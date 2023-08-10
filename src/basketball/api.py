import requests

def get_players():
    url = "http://www.balldontlie.io/api/v1/players"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_teams():
    url = "http://www.balldontlie.io/api/v1/teams"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_matches():
    url = "http://www.balldontlie.io/api/v1/matches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


