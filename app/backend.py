import mysql.connector
from mysql.connector import Error
import joblib
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

###################################################################################
# Web Scraping for live ESPN statistics #
###################################################################################

def create_connection():  
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='crystalball',
            user='root', 
            password=''  
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
    return None

def insert_team_stats(connection, teamID, games_played, games_won, ERA, OBP, Whip, Slg):
    cursor = connection.cursor()
    update_query = """
    UPDATE teams
    SET games_played = %s, games_won = %s, ERA = %s, OBP = %s, Whip = %s, Slg = %s
    WHERE teamID = %s
    """
    cursor.execute(update_query, (games_played, games_won, ERA, OBP, Whip, Slg, teamID))
    connection.commit()

def scrape_teamids():
    url = 'https://www.espn.com/mlb/stats/team/_/table/batting/sort/gamesPlayed/dir/desc'

    # Use Microsoft Edge
    edge_service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=edge_service)
    driver.get(url)

    time.sleep(5)  # Wait for the page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    table = soup.find('table', attrs={'class': 'Table Table--align-right Table--fixed Table--fixed-left'})
    if not table:
        print("Table with names not found")
        return []

    rows = table.find_all('tr')
    teamslist = []

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) == 0:
            print("Empty Row or no <td> elements found")
            continue

        img_tag = cols[1].find('img', attrs={'class': 'Image Logo Logo__sm'})
        if img_tag and 'title' in img_tag.attrs:
            teamID = img_tag['title'].strip()
            teamslist.append(teamID)

    return teamslist

def scrape_batting_stats():
    url = 'https://www.espn.com/mlb/stats/team/_/table/batting/sort/gamesPlayed/dir/desc'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Successfully connected to the website")
    else:
        print(f"Failed to connect to the website. Status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')

    if not soup:
        print("Failed to parse the content")
        return []

    table = soup.find('table', attrs={'class': 'Table Table--align-right'})
    if not table:
        print("Table not found")
        return []
    
    rows = table.find_all('tr')

    batting_stats = []

    for row in rows[1:]:
        cols = row.find_all('td')
        OBP = float(cols[13].text.strip())
        SLG = float(cols[14].text.strip())
        batting_stats.append((OBP, SLG))

    return batting_stats

def scrape_pitching_stats():
    url = 'https://www.espn.com/mlb/stats/team/_/view/pitching/table/pitching/sort/gamesPlayed/dir/desc'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to connect to the website. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', attrs={'class': 'Table Table--align-right'})
    if not table:
        print("Table not found")
        return []

    rows = table.find_all('tr')

    pitching_stats = []

    for row in rows[1:]:
        cols = row.find_all('td')
        try:
            games_played = int(cols[0].text.strip())
            games_won = int(cols[1].text.strip())
            ERA = float(cols[3].text.strip())
            Whip = float(cols[15].text.strip())
            pitching_stats.append((games_played, games_won, ERA, Whip))
        except (ValueError, IndexError):
            print(f"Error processing row data for row: {row}")
            continue

    return pitching_stats

def combine_stats(team_ids, batting_stats, pitching_stats):
    combined_stats = []
    for i in range(len(team_ids)):
        combined_stats.append((
            team_ids[i],
            pitching_stats[i][0],  # games_played
            pitching_stats[i][1],  # games_won
            pitching_stats[i][2],  # ERA
            batting_stats[i][0],  # OBP
            pitching_stats[i][3],  # WHIP
            batting_stats[i][1]  # SLG
        ))
    return combined_stats

###################################################################################
# End of Web Scraping for live ESPN statistics #
###################################################################################

###################################################################################
# Prediction Functionality #
###################################################################################

# Load the model and scaler
model = joblib.load('app/linear_regression_model.pkl')
scaler = joblib.load('app/scaler.pkl')

# Dictionary to map team abbreviations to full names
teamNames = {
    "ARI": "Arizona Diamondbacks",
    "ATL": "Atlanta Braves",
    "BAL": "Baltimore Orioles",
    "BOS": "Boston Red Sox",
    "CHC": "Chicago Cubs",
    "CIN": "Cincinnati Reds",
    "CLE": "Cleveland Guardians",
    "COL": "Colorado Rockies",
    "CHW": "Chicago White Sox",
    "DET": "Detroit Tigers",
    "HOU": "Houston Astros",
    "KC": "Kansas City Royals",
    "LAA": "Los Angeles Angels",
    "LAD": "Los Angeles Dodgers",
    "MIA": "Miami Marlins",
    "MIL": "Milwaukee Brewers",
    "MIN": "Minnesota Twins",
    "NYM": "New York Mets",
    "NYY": "New York Yankees",
    "OAK": "Oakland Athletics",
    "PHI": "Philadelphia Phillies",
    "PIT": "Pittsburgh Pirates",
    "SD": "San Diego Padres",
    "SEA": "Seattle Mariners",
    "SF": "San Francisco Giants",
    "STL": "St. Louis Cardinals",
    "TB": "Tampa Bay Rays",
    "TEX": "Texas Rangers",
    "TOR": "Toronto Blue Jays",
    "WSH": "Washington Nationals"
}

def get_team_stats(connection, team_name):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM teams WHERE teamID = %s"
    cursor.execute(query, (team_name,))
    result = cursor.fetchone()
    return result

def log5_win_probability(home_team_wp, away_team_wp):
    return (home_team_wp - home_team_wp * away_team_wp) / (home_team_wp + away_team_wp - 2 * home_team_wp * away_team_wp)

def predict_game(home_team_stats, away_team_stats):
    home_team_wp = home_team_stats['games_won'] / home_team_stats['games_played']
    away_team_wp = away_team_stats['games_won'] / away_team_stats['games_played']
    log5_probability = log5_win_probability(home_team_wp, away_team_wp)
    
    combined_stats = {
        'HomeTeamERA': home_team_stats['ERA'],
        'AwayTeamERA': away_team_stats['ERA'],
        'HomeTeamWHIP': home_team_stats['Whip'],
        'AwayTeamWHIP': away_team_stats['Whip'], 
        'HomeTeamSLG': home_team_stats['Slg'],
        'AwayTeamSLG': away_team_stats['Slg'],
        'HomeTeamOBP': home_team_stats['OBP'],
        'AwayTeamOBP': away_team_stats['OBP'],  
        'HomeTeamPythagoreanWP': home_team_stats['pythagorean_win_percentage'],
        'HomeTeamLog5WP': log5_probability
    }
    
    combined_stats_df = pd.DataFrame([combined_stats])
    combined_stats_scaled = scaler.transform(combined_stats_df)
    prediction = model.predict(combined_stats_scaled)[0]
    return round(prediction * 100, 2)

def get_mlb_schedule_today(api_key):
    today_date = datetime.today().strftime('%Y-%m-%d')
    url = f"https://api.sportsdata.io/v3/mlb/scores/json/GamesByDate/{today_date}"
    headers = {'Ocp-Apim-Subscription-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

def save_predictions(predictions):
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    cursor = connection.cursor()
    for prediction in predictions:
        cursor.execute("""
            INSERT INTO predictions (home_team, away_team, prediction, game_date)
            VALUES (%s, %s, %s, %s)
        """, (prediction['home_team'], prediction['away_team'], float(prediction['prediction']), datetime.today().date()))
    connection.commit()
    connection.close()

def save_past_predictions(connection):
    cursor = connection.cursor()
    cursor.execute("""
        INSERT IGNORE INTO past_predictions (home_team, away_team, prediction, game_date)
        SELECT home_team, away_team, prediction, game_date
        FROM predictions
    """)
    connection.commit()   

###################################################################################
# Main Function #
###################################################################################
def main():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return  

    pitching_stats = scrape_pitching_stats()
    batting_stats = scrape_batting_stats()
    team_ids = scrape_teamids()

    combined_stats = combine_stats(team_ids, batting_stats, pitching_stats)
    print("\nCombined Stats:")
    
    for stats in combined_stats:
        print(stats)

    for stats in combined_stats:
        insert_team_stats(connection, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6])

    api_key = '7f0204d9a6d946419f253fb71d198868'
    schedule = get_mlb_schedule_today(api_key)
    
    if not schedule:
        print("No games scheduled for today.")
        return
    
    #Save yesterdays predictions into past predictions table. 
    save_past_predictions(connection)

    # Clear existing predictions for today
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM predictions WHERE id > 0""")
    connection.commit()

    predictions = []

    for game in schedule:
        home_team_abbr = game['HomeTeam']
        away_team_abbr = game['AwayTeam']
        home_team = teamNames.get(home_team_abbr)
        away_team = teamNames.get(away_team_abbr)
        
        home_team_stats = get_team_stats(connection, home_team)
        away_team_stats = get_team_stats(connection, away_team)
        
        if home_team_stats and away_team_stats:
            prediction = predict_game(home_team_stats, away_team_stats)
            
            predictions.append({
                'home_team': home_team,
                'away_team': away_team,
                'prediction': prediction
            })
        else:
            print(f"Stats not found for one of the teams: {home_team}, {away_team}")
    
    save_predictions(predictions)

    if connection.is_connected():
        connection.close()

if __name__ == "__main__":
    main()
