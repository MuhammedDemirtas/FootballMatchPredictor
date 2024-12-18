from team_data import fetch_team_data, fetch_last_match_data, replace_turkish_characters

# Default number of matches to analyze for performance statistics
DEFAULT_MATCH_COUNT = 7

def predict_match_result(goal_prediction, team1, team2):
    """
    Predict the match result based on a given goal prediction.

    Parameters:
    - goal_prediction (int): Predicted goals for the first team.
    - team1 (str): Name of the first team.
    - team2 (str): Name of the second team.

    Returns:
    - str: A formatted string showing the predicted match result.
    """
    # Convert predicted goals to integers
    team1_goals = int(goal_prediction)
    # Adjust team2 goals based on team1 goals (if team1 scores, team2 scores one less; otherwise, 0)
    team2_goals = team1_goals - 1 if team1_goals > 0 else 0
    # Replace Turkish characters in team names for consistency
    team1 = replace_turkish_characters(team1)
    team2 = replace_turkish_characters(team2)
    # Return the formatted prediction
    return f"Predicted match result: {team1.capitalize()} {team1_goals} - {team2_goals} {team2.capitalize()}"

def analyze_two_teams(team1, team2, match_count):
    """
    Analyze and compare the performance of two teams over a specified number of matches.

    Parameters:
    - team1 (str): Name of the first team.
    - team2 (str): Name of the second team.
    - match_count (int): Number of matches to include in the analysis.

    Returns:
    - str: A detailed analysis report of both teams' performance.
    """
    # Replace Turkish characters in team names for consistency
    team1 = replace_turkish_characters(team1)
    team2 = replace_turkish_characters(team2)

    # Fetch data for both teams
    team1_data = fetch_team_data(team1)
    team2_data = fetch_team_data(team2)

    if team1_data is None or team2_data is None:
        # Return None if data for any team is unavailable
        return None

    # Wins, goals, and last match scores
    team1_wins, team1_goals, team1_last_match = team1_data
    team2_wins, team2_goals, team2_last_match = team2_data

    # Fetch the results for the last N matches
    team1_last_n_matches = fetch_last_match_data(team1, match_count)
    team2_last_n_matches = fetch_last_match_data(team2, match_count)

    if team1_last_n_matches is None or team2_last_n_matches is None:
        # Return None if data for the last matches is unavailable
        return None

    # Analyze Team 1's performance in the last N matches
    team1_wins_count = sum(1 for match in team1_last_n_matches if match > 0)
    team1_draws_count = sum(1 for match in team1_last_n_matches if match == 0)
    team1_losses_count = sum(1 for match in team1_last_n_matches if match < 0)

    # Analyze Team 2's performance in the last N matches
    team2_wins_count = sum(1 for match in team2_last_n_matches if match > 0)
    team2_draws_count = sum(1 for match in team2_last_n_matches if match == 0)
    team2_losses_count = sum(1 for match in team2_last_n_matches if match < 0)

    # Calculate total goals for both teams in the last N matches
    team1_total_goals = sum(match for match in team1_last_n_matches)
    team2_total_goals = sum(match for match in team2_last_n_matches)

    # Create a detailed report of the analysis
    result = f"{team1.capitalize()} Team Form:\nWins: {team1_wins_count}, Draws: {team1_draws_count}, Losses: {team1_losses_count}\n"
    result += f"{team2.capitalize()} Team Form:\nWins: {team2_wins_count}, Draws: {team2_draws_count}, Losses: {team2_losses_count}\n\n"
    result += f"{team1.capitalize()} Total Goals in Last {match_count} Matches: {team1_total_goals}\n"
    result += f"{team2.capitalize()} Total Goals in Last {match_count} Matches: {team2_total_goals}\n\n"

    # Add a note about the likelihood of an "Over" result (total goals > 18)
    if team1_total_goals + team2_total_goals > 18:
        result += "High probability of Over result\n\n"
    else:
        result += "Low probability of Over result\n\n"

    # Calculate and include the probability of 2 or more goals being scored
    goal_probability = (team1_total_goals + team2_total_goals) / (match_count * 2) * 100
    result += f"Probability of 2 or more goals: %{goal_probability:.2f}\n"

    return result
