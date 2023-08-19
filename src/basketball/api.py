import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime



def get_players():
    url = "http://www.balldontlie.io/api/v1/players"
    response = requests.get(url)
    if response.status_code == 200:
        players_data = response.json()
        players = players_data['data']
        return players
    else:
        return None
    
def get_player_detail(player_id):
    url = f"https://www.balldontlie.io/api/v1/players/{player_id}"
    response = requests.get(url)
    if response.status_code == 200:
        player = response.json()
        return player
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
    
def get_team_detail(team_id):
    url = f"https://www.balldontlie.io/api/v1/teams/{team_id}"
    response = requests.get(url)
    if response.status_code == 200:
        team = response.json()
        return team
    else:
        return None
  
def get_matches():
    url = "http://www.balldontlie.io/api/v1/games"
    response = requests.get(url)
    if response.status_code == 200:
        matches_data = response.json()
        matches = matches_data["data"]

        for match in matches:
            date_str = match["date"]
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            formatted_date = date_obj.strftime('%d %B %Y')
            match["date"] = formatted_date
        
        return matches
    else:
        return None


def get_match_detail(match_id):
    url = f"https://www.balldontlie.io/api/v1/games/{match_id}"
    response = requests.get(url)
    if response.status_code == 200:
        match = response.json()

        date_str = match["date"]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %Z')
        formatted_date = date_obj.strftime('%d %B %Y')
        match["date"] = formatted_date

        return match
    else:
        return None
"""
@api_view(['GET'])
def team_players(request, team_id):
    players_data = []
    page = 0

    
    while True:
        response = requests.get(f"https://www.balldontlie.io/api/v1/players?page={page}")
        all_players_data = response.json()['data']
        
        
        filtered_players = [player for player in all_players_data if player['team']['id'] == team_id]
        players_data.extend(filtered_players)
        
        
        if response.json().get('meta').get('next_page') is None:
            break
            
        page += 1

    return Response(players_data, status=status.HTTP_200_OK)
"""