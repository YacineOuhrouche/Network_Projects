import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

# URLs for NBA, NFL, MLB, and NHL stats
url_stats_nba = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
url_stats_nfl = "https://www.pro-football-reference.com/years/2024/passing.htm"
url_stats_mlb = "https://www.baseball-reference.com/leagues/MLB_2024_batting.shtml"
url_stats_nhl = "https://www.hockey-reference.com/leagues/NHL_2024_skaters.html"

# Function to format stats with proper alignment
def format_stat_line(player_name, *stats):
    return f"{player_name.ljust(25)} | " + " | ".join([str(stat).ljust(8) for stat in stats])

# Function to scrape top NBA player stats
def get_top_player_stats_nba(num_players=5):
    output = "\n" + "="*80 + "\n"
    output += "Top NBA Player Stats (2024 Season)".center(80) + "\n"
    output += "="*80 + "\n"
    
    try:
        response = requests.get(url_stats_nba)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'per_game_stats'})
        if table:
            output += "Player Name                  | Points PPG | Assists APG | Rebounds RPG\n"
            output += "-" * 80 + "\n"
            rows = table.find_all('tr')[1:num_players + 1]  # Get the top players
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    points = cols[28].text.strip()  # Points per game (PTS column)
                    assists = cols[23].text.strip()  # Assists per game (AST column)
                    rebounds = cols[21].text.strip()  # Rebounds per game (TRB column)
                    output += format_stat_line(player_name, points, assists, rebounds) + "\n"
        else:
            output += "Could not find the player stats table.\n"
    
    except requests.exceptions.RequestException as e:
        output += f"Error fetching NBA player stats: {e}\n"

    return output

# Function to scrape top NFL player stats
def get_top_player_stats_nfl(num_players=5):
    output = "\n" + "="*80 + "\n"
    output += "Top NFL Player Stats (2024 Season)".center(80) + "\n"
    output += "="*80 + "\n"
    
    try:
        response = requests.get(url_stats_nfl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'passing'})
        if table:
            output += "Player Name                  | Yards Passing | Touchdowns TDs | Interceptions INTs\n"
            output += "-" * 80 + "\n"
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    pass_yards = cols[1].text.strip()  # Passing yards
                    touchdowns = cols[2].text.strip()  # Touchdowns
                    interceptions = cols[3].text.strip()  # Interceptions
                    output += format_stat_line(player_name, pass_yards, touchdowns, interceptions) + "\n"
        else:
            output += "Could not find the player stats table.\n"
    
    except requests.exceptions.RequestException as e:
        output += f"Error fetching NFL player stats: {e}\n"

    return output

# Function to scrape top MLB player stats
def get_top_player_stats_mlb(num_players=5):
    output = "\n" + "="*80 + "\n"
    output += "Top MLB Player Stats (2024 Season)".center(80) + "\n"
    output += "="*80 + "\n"
    
    try:
        response = requests.get(url_stats_mlb)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            output += "Player Name                  | Batting AVG | Home Runs HR | RBIs\n"
            output += "-" * 80 + "\n"
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    avg = cols[1].text.strip()  # Batting Average
                    home_runs = cols[3].text.strip()  # Home Runs
                    rbi = cols[4].text.strip()  # RBIs
                    output += format_stat_line(player_name, avg, home_runs, rbi) + "\n"
        else:
            output += "Could not find the player stats table.\n"
    
    except requests.exceptions.RequestException as e:
        output += f"Error fetching MLB player stats: {e}\n"

    return output

# Function to scrape top NHL player stats
def get_top_player_stats_nhl(num_players=5):
    output = "\n" + "="*80 + "\n"
    output += "Top NHL Player Stats (2024 Season)".center(80) + "\n"
    output += "="*80 + "\n"
    
    try:
        response = requests.get(url_stats_nhl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            output += "Player Name                  | Goals G | Assists A | Points P\n"
            output += "-" * 80 + "\n"
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    goals = cols[1].text.strip()  # Goals
                    assists = cols[2].text.strip()  # Assists
                    points = cols[3].text.strip()  # Points
                    output += format_stat_line(player_name, goals, assists, points) + "\n"
        else:
            output += "Could not find the player stats table.\n"
    
    except requests.exceptions.RequestException as e:
        output += f"Error fetching NHL player stats: {e}\n"

    return output

# Function to update the output box with stats based on the selected league
def update_stats(selected_league):
    output_box.delete(1.0, tk.END)
    
    if selected_league == "NBA":
        output_box.insert(tk.END, get_top_player_stats_nba())
    elif selected_league == "NFL":
        output_box.insert(tk.END, get_top_player_stats_nfl())
    elif selected_league == "MLB":
        output_box.insert(tk.END, get_top_player_stats_mlb())
    elif selected_league == "NHL":
        output_box.insert(tk.END, get_top_player_stats_nhl())

# Create main window
root = tk.Tk()
root.title("Top Player Stats (2024 Season)")
root.geometry("1000x700")

# Set background color
root.config(bg="#f0f0f0")

# Create a title label
title_font = font.Font(family="Helvetica", size=18, weight="bold")
title_label = tk.Label(root, text="Top Player Stats (2024 Season)", font=title_font, bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

# Create a frame for the dropdown and output
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

# Create a dropdown menu to select the league
leagues = ["NBA", "NFL", "MLB", "NHL"]
selected_league = tk.StringVar(root)
selected_league.set(leagues[0])  # Set default value

league_menu = tk.OptionMenu(frame, selected_league, *leagues)
league_menu.config(font=("Helvetica", 12), bg="#4CAF50", fg="white")
league_menu.grid(row=0, column=0, padx=10)

# Create a button to refresh stats based on selected league
refresh_button = tk.Button(frame, text="Refresh Stats", font=("Helvetica", 12), bg="#4CAF50", fg="white", 
                            command=lambda: update_stats(selected_league.get()))
refresh_button.grid(row=0, column=1, padx=10)

# Create a scrolled text widget for displaying the output
output_box = scrolledtext.ScrolledText(root, width=120, height=25, wrap=tk.WORD, font=("Courier New", 10))
output_box.pack(padx=20, pady=20)

# Run the GUI
root.mainloop()
