import requests

def get_players():
    url = "http://www.balldontlie.io/api/v1/players"
    response = requests.get(url)
    if response.status_code == 200:
        players_data = response.json()
        players = players_data['data']
        return players
    else:
        return None

def get_teams():
    url = "http://www.balldontlie.io/api/v1/teams"
    response = requests.get(url)
    if response.status_code == 200:
        teams_data = response.json()
        teams = teams_data["data"]
        return teams
    else:
        return None

def get_matches():
    url = "http://www.balldontlie.io/api/v1/games"
    response = requests.get(url)
    if response.status_code == 200:
        matches_data = response.json()
        matches = matches_data["data"]
        return matches
    else:
        return None


