from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
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
def scrape_teamids(): #This will get the names and put it on a list
    url = 'https://www.espn.com/mlb/stats/team/_/table/batting/sort/gamesPlayed/dir/desc' 

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url)
    
    time.sleep(5)

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

        img_tag = cols[1].find('img', attrs={'class' : 'Image Logo Logo__sm'})
        if img_tag:
            if 'title' in img_tag.attrs:
                team_name = img_tag['title'].strip()
                teamId = team_name[:3].upper() 
                teamslist.append((teamId, team_name))
            else:
                print ("Title attribute not found in img tag")
        else:
            print("Img tag not found")

    return teamslist

def scrape_batting_stats(): #grabbing the batting stats needed for algorithm and adding to list
    url = 'https://www.espn.com/mlb/stats/team/_/table/batting/sort/gamesPlayed/dir/desc' 

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

    batting_stats = []

    for row in rows[1:]: 
        cols = row.find_all('td')
        OBP = float(cols[13].text.strip())  
        SLG = float(cols[14].text.strip())  
        batting_stats.append((OBP, SLG))

    return (batting_stats) 

def scrape_pitching_stats(): #grabbing pitching stats and putting on list
    url = 'https://www.espn.com/mlb/stats/team/_/view/pitching/table/pitching/sort/gamesPlayed/dir/desc'  
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

    pitching_stats = []

    for row in rows[1:]: 
        cols = row.find_all('td')
        games_played = int(cols[0].text.strip())
        games_won = int(cols[1].text.strip())
        ERA = float(cols[3].text.strip())
        Whip = float(cols[15].text.strip()) 
        pitching_stats.append(( games_played, games_won, ERA, Whip))
    

    return pitching_stats

def combine_stats(team_ids, batting_stats, pitching_stats):
    combined_stats = []
    for i in range(len(team_ids)):
        combined_stats.append((
            team_ids[i][0],  # teamId
            team_ids[i][1],  # teamName
            pitching_stats[i][0],  # games_played
            pitching_stats[i][1],  # games_won
            pitching_stats[i][2],  # ERA
            batting_stats[i][0],  # OBP
            pitching_stats[i][3],  # WHIP
            batting_stats[i][1]  # SLG
        ))
    return combined_stats


def main():

    pitching_stats = scrape_pitching_stats()
    batting_stats = scrape_batting_stats()
    team_ids = scrape_teamids()

    combined_stats = combine_stats(team_ids, batting_stats, pitching_stats)
    print("\nCombined Stats:")
    for stats in combined_stats:
        print(stats)

'''
    connection = create_connection()
    if connection:
        teamslist = scrape_teamslist()
        batting_stats = scrape_batting_stats()
        pitching_stats = scrape_pitching_stats()

        combined_stats = {}
        for team in teamslist:
            teamID, name = team
            combined_stats[teamID] = {'name': name}
        for team in batting_stats:
            OBP, SLG = team
            combined_stats[teamID] = {'OBP': OBP, 'SLG': SLG}
        
        for team in pitching_stats:
            games_played, games_won, ERA, Whip = team
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
    