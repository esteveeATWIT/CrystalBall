from flask import Flask, jsonify, render_template
import pandas as pd
import joblib
import mysql.connector
from mysql.connector import Error
import requests
from datetime import datetime

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

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

# Function to create a database connection
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

# Function to get team statistics from the database
def get_team_stats(connection, team_name):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM teams WHERE teamID = %s"
    cursor.execute(query, (team_name,))
    result = cursor.fetchone()
    return result

# Function to calculate win probability using the Log5 method
def log5_win_probability(home_team_wp, away_team_wp):
    return (home_team_wp - home_team_wp * away_team_wp) / (home_team_wp + away_team_wp - 2 * home_team_wp * away_team_wp)

# Function to predict the outcome of a game
def predict_game(home_team_stats, away_team_stats):
    home_team_wp = home_team_stats['games_won'] / home_team_stats['games_played']
    away_team_wp = away_team_stats['games_won'] / away_team_stats['games_played']
    log5_probability = log5_win_probability(home_team_wp, away_team_wp)
    
    # Combine relevant statistics for prediction
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
    
    # Scale the combined statistics and make a prediction
    combined_stats_df = pd.DataFrame([combined_stats])
    combined_stats_scaled = scaler.transform(combined_stats_df)
    prediction = model.predict(combined_stats_scaled)[0]
    return round(prediction*100, 4)

# Function to get today's MLB schedule using an API
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

# Function to save predictions to the database
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

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the project page
@app.route('/project')
def project():
    return render_template('project.html')

# Route to get today's predictions
@app.route('/get_predictions', methods=['GET'])
def get_predictions():
    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Failed to connect to the database."}), 500
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT home_team, away_team, prediction
        FROM predictions
        WHERE game_date = %s
    """, (datetime.today().date(),))
    predictions = cursor.fetchall()
    connection.close()
    
    return jsonify(predictions)

# Main function to orchestrate the prediction process
def main():
    api_key = '7f0204d9a6d946419f253fb71d198868'
    schedule = get_mlb_schedule_today(api_key)
    
    if not schedule:
        print("No games scheduled for today.")
        return

    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    # Clear existing predictions for today
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM predictions WHERE game_date = %s
    """, (datetime.today().date(),))
    connection.commit()
    
    predictions = []

    # Iterate over each game in the schedule and make predictions
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
    
    # Save the new predictions to the database
    save_predictions(predictions)
    connection.close()
    
if __name__ == '__main__':
    main()
    app.run(debug=True)
