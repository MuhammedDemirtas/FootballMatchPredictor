from team_data import fetch_team_data, fetch_last_match_data, replace_turkish_characters

DEFAULT_MATCH_COUNT = 7

def predict_match_result(goal_prediction, team1, team2):
    team1_goals = int(goal_prediction)
    team2_goals = team1_goals - 1 if team1_goals > 0 else 0
    team1 = replace_turkish_characters(team1)
    team2 = replace_turkish_characters(team2)
    return f"Predicted match result: {team1.capitalize()} {team1_goals} - {team2_goals} {team2.capitalize()}"

def analyze_two_teams(team1, team2, match_count):
    team1 = replace_turkish_characters(team1)
    team2 = replace_turkish_characters(team2)

    # Fetch team data
    team1_data = fetch_team_data(team1)
    team2_data = fetch_team_data(team2)

    if team1_data is None or team2_data is None:
        return None

    # Wins, goals, and last match scores
    team1_wins, team1_goals, team1_last_match = team1_data
    team2_wins, team2_goals, team2_last_match = team2_data

    # Analyze results for the last N matches
    team1_last_n_matches = fetch_last_match_data(team1, match_count)
    team2_last_n_matches = fetch_last_match_data(team2, match_count)

    if team1_last_n_matches is None or team2_last_n_matches is None:
        return None

    # Analyze Team 1's performance
    team1_wins_count = sum(1 for match in team1_last_n_matches if match > 0)
    team1_draws_count = sum(1 for match in team1_last_n_matches if match == 0)
    team1_losses_count = sum(1 for match in team1_last_n_matches if match < 0)

    # Analyze Team 2's performance
    team2_wins_count = sum(1 for match in team2_last_n_matches if match > 0)
    team2_draws_count = sum(1 for match in team2_last_n_matches if match == 0)
    team2_losses_count = sum(1 for match in team2_last_n_matches if match < 0)

    # Total goals in the last N matches
    team1_total_goals = sum(match for match in team1_last_n_matches)
    team2_total_goals = sum(match for match in team2_last_n_matches)

    result = f"{team1.capitalize()} Team Form:\nWins: {team1_wins_count}, Draws: {team1_draws_count}, Losses: {team1_losses_count}\n"
    result += f"{team2.capitalize()} Team Form:\nWins: {team2_wins_count}, Draws: {team2_draws_count}, Losses: {team2_losses_count}\n\n"
    result += f"{team1.capitalize()} Total Goals in Last {match_count} Matches: {team1_total_goals}\n"
    result += f"{team2.capitalize()} Total Goals in Last {match_count} Matches: {team2_total_goals}\n\n"

    if team1_total_goals + team2_total_goals > 18:
        result += "High probability of Over result\n\n"
    else:
        result += "Low probability of Over result\n\n"

    goal_probability = (team1_total_goals + team2_total_goals) / (match_count * 2) * 100
    result += f"Probability of 2 or more goals: %{goal_probability:.2f}\n"

    return result
