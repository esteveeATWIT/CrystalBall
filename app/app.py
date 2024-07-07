from flask import Flask, jsonify, render_template
import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

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

# Main function to launch website
def main():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
if __name__ == '__main__':
    main()
    app.run(debug=True)
