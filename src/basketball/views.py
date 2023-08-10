from django.shortcuts import render
from .api import get_players, get_player_detail
from .api import get_teams, get_team_detail
from .api import get_matches, get_match_detail

def players_view(request):
    players = get_players()
    return render(request, "players.html", {"players": players})

def player_detail_view(request, player_id):
    player = get_player_detail(player_id)
    return render(request, "player_detail.html", {"player": player})


def teams_view(request):
    teams = get_teams()
    return render(request, "teams.html", {"teams": teams})

def team_detail_view(request, team_id):
    team = get_team_detail(team_id)
    return render(request, "team_detail.html", {"team": team})

def matches_view(request):
    matches = get_matches()
    return render(request, "matches.html", {"matches": matches})

def match_detail_view(request, match_id):
    match = get_match_detail(match_id)
    return render(request, "match_detail.html", {"match": match})

