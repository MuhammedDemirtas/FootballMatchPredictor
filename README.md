# Football Match Predictor

This project is a Football Match Predictor application that analyzes past match data to predict the outcome of upcoming football matches. It fetches live data from an online source, evaluates the performance of the teams, and predicts match results based on historical statistics. The application features a user-friendly graphical interface for easy interaction.

## Features

- **Team Performance Insights:**
  - Displays detailed statistics such as the number of wins, losses, and draws for each team in their last N matches.
  - Shows the total number of goals scored by each team.

- **Match Prediction:**
  - Calculates the probability of more than 2 goals in a match.
  - Assesses the likelihood of an "Over" result based on historical performance.

- **Improved User Interface:**
  - Intuitive and interactive GUI for easy input of team names and match count.
  - Clear display of prediction results.

- **Real-Time Data:**
  - Fetches live match data and dynamically updates predictions based on the teams' current performance.

## Installation

To get started, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MuhammedDemirtas/FootballMatchPredictor.git
   cd FootballMatchPredictor
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
2. Run the application:
   ```bash
   python main.py
This will launch the Football Match Predictor GUI, where you can input the teams and analyze their past match performances to predict future outcomes.

## Code Overview
main.py

    Main entry point for the application. Controls the overall prediction process.
    Fetches match data from an online source using web scraping.
    Analyzes past performances and predicts the match outcome, including insights into the total number of goals and the likelihood of more than 2 goals.

requirements.txt

    Contains all necessary libraries and dependencies for the application.
    Ensures that the application has the required libraries installed, such as requests and beautifulsoup4 for web scraping, and tkinter for the graphical user interface.

team_data.py

    Contains functions for fetching team match data from an online source.
    Analyzes the number of wins, losses, and draws for each team and the total goals scored.
    Functions include:
        fetch_team_data: Fetches data about a team’s past matches.
        fetch_last_match_data: Fetches data about the team’s last N matches.
        replace_turkish_characters: Handles Turkish character replacements for proper matching.

match_prediction.py

    Contains the logic for predicting match outcomes based on team data.
    Includes functions to calculate the predicted scoreline and analyze the match performance of two teams.

ui.py

    Handles the graphical user interface (GUI) using tkinter.
    Allows the user to input team names and match count, then displays the predicted results.

License

This project is licensed under the MIT License.

For more details, visit the GitHub repository.
Developer

    M. Demirtas

