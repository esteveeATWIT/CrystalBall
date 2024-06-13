import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

'''
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
    
'''
'''
# Function to insert data into the database
def insert_team_stats(connection, teamID, name, games_played, games_won, ERA, OBP, Whip, Slg):
    cursor = connection.cursor()
    insert_query = """
    UPDATE teams
    SET games_played = %s, games_won = %s, ERA = %s, OBP = %s, Whip = %s, Slg = %s
    WHERE teamID = %s
    """
    cursor.execute(insert_query, (games_played, games_won, ERA, OBP, Whip, Slg, teamID))
    connection.commit()
'''
# Web scraping setup
def scrape_batting_stats():
    url = 'https://www.espn.com/mlb/stats/team' 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', attrs={'class': 'Table Table'}) 
    if not table:
        print("Table not found")
        return []
    rows = table.find_all('tr')

    batting_stats = []

    for row in rows[1:]: 
        cols = row.find_all('td')
        teamID = cols[0].text.strip()[:3]
        name = cols[0].text.strip()
        OBP = float(cols[13].text.strip())  
        SLG = float(cols[14].text.strip())  

        batting_stats.append((teamID, name, OBP, SLG))
    
    return batting_stats

def scrape_pitching_stats():
    url = 'https://www.espn.com/mlb/stats/team/_/view/pitching'  
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table') 
    rows = table.find_all('tr')

    pitching_stats = []

    for row in rows[1:]: 
        cols = row.find_all('td')
        teamID = cols[0].text.strip()[:3]
        name = cols[0].text.strip()
        games_played = int(cols[1].text.strip())
        games_won = int(cols[2].text.strip())
        ERA = float(cols[3].text.strip())
        Whip = float(cols[6].text.strip()) 

        pitching_stats.append((teamID, name, games_played, games_won, ERA, Whip))
    
    return pitching_stats



def main():
    url = 'https://www.espn.com/mlb/stats/team' 
    #header for bypassing the website so we can connect succesfully (makes the request look like it's coming from a real browser)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Successfully connected to the website")
    else:
        print(f"Failed to connect to the website. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    if not soup:
        print("Failed to parse the content")
        return

    table = soup.find('table', attrs={'class': 'Table Table--align-right'}) 
    if not table:
        print("Table not found")
        return []
    rows = table.find_all('tr')

    testing = []

    for row in rows[1:]: 
        cols = row.find_all('td')
        teamID = cols[0].text.strip()[:3]
        name = cols[0].text.strip()
        OBP = float(cols[13].text.strip())  
        SLG = float(cols[14].text.strip())  

        testing.append((teamID, name, OBP, SLG))
    
    print (testing) 
'''
    connection = create_connection()
    if connection:
        batting_stats = scrape_batting_stats()
        pitching_stats = scrape_pitching_stats()

        combined_stats = {}
        for team in batting_stats:
            teamID, name, OBP, SLG = team
            combined_stats[teamID] = {'name': name, 'OBP': OBP, 'SLG': SLG}
        
        for team in pitching_stats:
            teamID, name, games_played, games_won, ERA, Whip = team
            if teamID in combined_stats:
                combined_stats[teamID].update({
                    'games_played': games_played,
                    'games_won': games_won,
                    'ERA': ERA,
                    'Whip': Whip
                })

        for teamID, stats in combined_stats.items():
            insert_team_stats(
                connection,
                teamID,
                stats['name'],
                stats.get('games_played', None),
                stats.get('games_won', None),
                stats.get('ERA', None),
                stats['OBP'],
                stats['Whip'],
                stats['SLG']
            )
        connection.close()
        '''

if __name__ == "__main__":
    main()
    