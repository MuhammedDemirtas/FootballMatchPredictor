import requests
from bs4 import BeautifulSoup
import os

def fetch_team_data(team):
    clear_screen()
    url = f"https://www.sporx.com/{team}-fiksturu-ve-mac-sonuclari"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    matches = soup.find_all("tr")
    win_count = 0
    total_goals = 0
    last_match_score = None

    for match in matches:
        score_element = match.find("a", class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")
        if score_element:
            score = score_element.get_text(strip=True)
            goal_counts = score.split("-")
            if len(goal_counts) == 2 and all(count.strip() for count in goal_counts):
                try:
                    home_goals = int(goal_counts[0])
                    away_goals = int(goal_counts[1])
                except ValueError:
                    continue

                home_team = match.find("td", class_="text-start w-25").find("a").get_text(strip=True)
                away_team = match.find("td", class_="text-end w-25").find("a").get_text(strip=True)

                if team.lower() == home_team.lower():
                    total_goals += home_goals
                    if home_goals > away_goals:
                        win_count += 1
                    last_match_score = f"{home_team} {score} {away_team}\n"
                elif team.lower() == away_team.lower():
                    total_goals += away_goals
                    if home_goals < away_goals:
                        win_count += 1
                    last_match_score = f"{away_team} {score} {home_team}\n"

    if win_count == 0:
        return None, None, None
    else:
        return win_count, total_goals, last_match_score

def fetch_last_match_data(team, match_count):
    url = f"https://www.sporx.com/{team}-fiksturu-ve-mac-sonuclari"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    matches = soup.find_all("tr")

    last_match_goal_counts = []
    match_counter = 0

    for match in reversed(matches):
        score_element = match.find("a", class_="d-block rounded bg-sporx text-white fw-bolder py-1 px-1 text-nowrap")

        if score_element:
            score = score_element.get_text(strip=True)
            goal_counts = score.split("-")

            if len(goal_counts) == 2 and all(count.strip() for count in goal_counts):
                try:
                    home_goals = int(goal_counts[0])
                    away_goals = int(goal_counts[1])
                except ValueError:
                    continue

                home_team = match.find("td", class_="text-start w-25").find("a").get_text(strip=True)
                away_team = match.find("td", class_="text-end w-25").find("a").get_text(strip=True)

                if team.lower() == replace_turkish_characters(home_team.lower()):
                    last_match_goal_counts.append(home_goals)  # Add to the end
                    match_counter += 1
                elif team.lower() == replace_turkish_characters(away_team.lower()):
                    last_match_goal_counts.append(away_goals)  # Add to the end
                    match_counter += 1

                if match_counter >= match_count:
                    break

    if last_match_goal_counts:
        return last_match_goal_counts
    else:
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def replace_turkish_characters(team_name):
    team_name = team_name.replace("ı", "i")
    team_name = team_name.replace("ç", "c")
    team_name = team_name.replace("ş", "s")
    team_name = team_name.replace("ğ", "g")
    team_name = team_name.replace("ü", "u")
    team_name = team_name.replace("ö", "o")
    return team_name.replace(" ", "-")  # Replace spaces with '-'