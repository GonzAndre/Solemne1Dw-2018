from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('add_player', views.add_player, name="player_add"),
    path('add_coach', views.add_coach, name="Coach_add"),
    path('add_team', views.add_team, name="Team_add"),
    path('edit_player/<int:player_id>', views.edit_player, name="Player_edit"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
]
