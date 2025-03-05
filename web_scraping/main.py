import requests
from bs4 import BeautifulSoup

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
    print("\n" + "="*80)
    print("Top NBA Player Stats (2024 Season)".center(80))
    print("="*80)
    
    try:
        response = requests.get(url_stats_nba)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'per_game_stats'})
        if table:
            print("Player Name                  | Points PPG | Assists APG | Rebounds RPG")
            print("-" * 80)
            rows = table.find_all('tr')[1:num_players + 1]  # Get the top players
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    points = cols[28].text.strip()  # Points per game (PTS column)
                    assists = cols[23].text.strip()  # Assists per game (AST column)
                    rebounds = cols[21].text.strip()  # Rebounds per game (TRB column)
                    print(format_stat_line(player_name, points, assists, rebounds))
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NBA player stats: {e}")

# Function to scrape top NFL player stats
def get_top_player_stats_nfl(num_players=5):
    print("\n" + "="*80)
    print("Top NFL Player Stats (2024 Season)".center(80))
    print("="*80)
    
    try:
        response = requests.get(url_stats_nfl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'passing'})
        if table:
            print("Player Name                  | Yards Passing | Touchdowns TDs | Interceptions INTs")
            print("-" * 80)
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    pass_yards = cols[1].text.strip()  # Passing yards
                    touchdowns = cols[2].text.strip()  # Touchdowns
                    interceptions = cols[3].text.strip()  # Interceptions
                    print(format_stat_line(player_name, pass_yards, touchdowns, interceptions))
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFL player stats: {e}")

# Function to scrape top MLB player stats
def get_top_player_stats_mlb(num_players=5):
    print("\n" + "="*80)
    print("Top MLB Player Stats (2024 Season)".center(80))
    print("="*80)
    
    try:
        response = requests.get(url_stats_mlb)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            print("Player Name                  | Batting AVG | Home Runs HR | RBIs")
            print("-" * 80)
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    avg = cols[1].text.strip()  # Batting Average
                    home_runs = cols[3].text.strip()  # Home Runs
                    rbi = cols[4].text.strip()  # RBIs
                    print(format_stat_line(player_name, avg, home_runs, rbi))
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching MLB player stats: {e}")

# Function to scrape top NHL player stats
def get_top_player_stats_nhl(num_players=5):
    print("\n" + "="*80)
    print("Top NHL Player Stats (2024 Season)".center(80))
    print("="*80)
    
    try:
        response = requests.get(url_stats_nhl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            print("Player Name                  | Goals G | Assists A | Points P")
            print("-" * 80)
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    goals = cols[1].text.strip()  # Goals
                    assists = cols[2].text.strip()  # Assists
                    points = cols[3].text.strip()  # Points
                    print(format_stat_line(player_name, goals, assists, points))
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NHL player stats: {e}")

# Run the functions with desired number of players
get_top_player_stats_nba(num_players=5)  # NBA
get_top_player_stats_nfl(num_players=5)  # NFL
get_top_player_stats_mlb(num_players=5)  # MLB
get_top_player_stats_nhl(num_players=5)  # NHL
