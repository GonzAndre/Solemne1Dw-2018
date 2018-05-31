from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('list_coach', views.listcoach, name="coach_list"),
    path('list_team', views.listteam, name="team_list"),
    path('add_player', views.add_player, name="player_add"),
    path('add_coach', views.add_coach, name="coach_add"),
    path('add_team', views.add_team, name="team_add"),
    path('edit_player/<int:player_id>', views.edit_player, name="Player_edit"),
    path('edit_coach/<int:coach_id>', views.edit_coach, name="Coach_edit"),
    path('edit_team/<int:team_id>', views.edit_team, name="team_edit"),
    path('view_player/<int:player_id>', views.detail, name="player_detail"),
    path('view_coach/<int:coach_id>', views.detail_coach, name="coach_detail"),
    path('view_team/<int:team_id>', views.detail_team, name="team_detail"),
    path('delete/<int:id>', views.Delete, name="Delete"),
    path('delete_coach/<int:coach_id>',views.Delete_coach, name='Delete_coach'),
    path('delete_team/<int:team_id>',views.Delete_team, name='Delete_team'),
]