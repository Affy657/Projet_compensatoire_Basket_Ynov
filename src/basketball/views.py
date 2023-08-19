from django.shortcuts import render
from .api import get_players, get_player_detail
from .api import get_teams, get_team_detail
from .api import get_matches, get_match_detail
from django.contrib.auth.decorators import login_required

@login_required
def players_view(request):
    players = get_players()
    return render(request, "players.html", {"players": players})

@login_required
def player_detail_view(request, player_id):
    player = get_player_detail(player_id)
    return render(request, "player_detail.html", {"player": player})

@login_required
def teams_view(request):
    teams = get_teams()
    return render(request, "teams.html", {"teams": teams})

@login_required
def team_detail_view(request, team_id):
    team = get_team_detail(team_id)
    return render(request, "team_detail.html", {"team": team})

@login_required
def matches_view(request):
    matches = get_matches()
    return render(request, "matches.html", {"matches": matches})

@login_required
def match_detail_view(request, match_id):
    match = get_match_detail(match_id)
    return render(request, "match_detail.html", {"match": match})

