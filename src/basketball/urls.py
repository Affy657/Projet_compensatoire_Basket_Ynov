from django.urls import path
from .views import players_view,  teams_view,  matches_view
from .views import player_detail_view,team_detail_view,match_detail_view

urlpatterns = [
    path('players/', players_view, name='players_view'),
    path('players/<int:player_id>/', player_detail_view, name='player_detail'),
    path('teams/', teams_view, name='teams_view'),
    path('teams/<int:team_id>/', team_detail_view, name='team_detail'),
    path('matches/', matches_view, name='matches_view'),
    path('matches/<int:match_id>/', match_detail_view, name='match_detail'),
]
