import tkinter as tk
from tkinter import ttk, messagebox
from match_prediction import analyze_two_teams, predict_match_result

# Main function to initialize and run the GUI application
def main():
    global team1_entry, team2_entry, match_count_entry, result_label

    # Create the main application window
    root = tk.Tk()
    root.title("Football Match Predictor")

    # Create a frame for the widgets and set padding
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Label and entry for Team 1
    ttk.Label(frame, text="Team 1:").grid(row=0, column=0, sticky=tk.W)
    team1_entry = ttk.Entry(frame)
    team1_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    # Label and entry for Team 2
    ttk.Label(frame, text="Team 2:").grid(row=1, column=0, sticky=tk.W)
    team2_entry = ttk.Entry(frame)
    team2_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    # Label and entry for Match Count with a default value
    ttk.Label(frame, text="Match Count:").grid(row=2, column=0, sticky=tk.W)
    match_count_entry = ttk.Entry(frame)
    match_count_entry.insert(0, "7")  # Default match count
    match_count_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

    # Button to analyze the teams
    analyze_button = ttk.Button(frame, text="Analyze Teams", command=analyze_button_click)
    analyze_button.grid(row=3, columnspan=2, sticky=(tk.W, tk.E))

    # Label to display the results of the analysis
    result_label = ttk.Label(frame, text="", justify=tk.LEFT)
    result_label.grid(row=4, columnspan=2, sticky=(tk.W, tk.E))

    # Start the main event loop
    root.mainloop()

# Function to handle the button click event for team analysis
def analyze_button_click():
    team1 = team1_entry.get()
    team2 = team2_entry.get()
    match_count = int(match_count_entry.get())

    # Ensure that both teams are entered
    if not team1 or not team2:
        messagebox.showerror("Error", "Please enter the teams.")
        return

    # Call the analysis function and display the results
    result = analyze_two_teams(team1, team2, match_count)
    if result:
        result_label.config(text=result)
