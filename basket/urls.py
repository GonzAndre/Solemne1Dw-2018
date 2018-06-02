from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('list', views.index, name="player_list"),
    path('list_coach', views.listcoach, name="coach_list"),
    path('list_team', views.listteam, name="team_list"),
    path('list_match', views.listmatch, name="match_list"),
    path('list_rostermatch', views.listrostermatch, name="rostermatch_list"),
    path('list_roster', views.listroster, name="roster_list"),
    path('add_player', views.add_player, name="player_add"),
    path('add_coach', views.add_coach, name="coach_add"),
    path('add_team', views.add_team, name="team_add"),
    path('add_match', views.add_match, name='match_add'),
    path('add_roster', views.add_roster, name='roster_add'),
    path('add_rostermatch', views.add_rostermatch, name='rostermatch_add'),
    path('edit_player/<int:player_id>', views.edit_player, name="Player_edit"),
    path('edit_coach/<int:coach_id>', views.edit_coach, name="Coach_edit"),
    path('edit_team/<int:team_id>', views.edit_team, name="team_edit"),
    path('edit_match/<int:match_id>', views.edit_match, name='match_edit'),
    path('edit_roster/<int:roster_id>', views.edit_roster, name='roster_edit'),
    path('edit_rostermatch/<int:rostermatch_id>', views.edit_rostermatch, name='rostermatch_edit'),
    path('view_player/<int:player_id>', views.detail, name="player_detail"),
    path('view_coach/<int:coach_id>', views.detail_coach, name="coach_detail"),
    path('view_team/<int:team_id>', views.detail_team, name="team_detail"),
    path('delete/<int:id>', views.Delete, name="Delete"),
    path('delete_coach/<int:coach_id>',views.Delete_coach, name='Delete_coach'),
    path('delete_team/<int:team_id>',views.Delete_team, name='Delete_team'),
    path('delete_match/<int:match_id>',views.Delete_match, name='Delete_match'),
    path('delete_roster/<int:roster_id>',views.Delete_roster, name='Delete_roster'),
    path('delete_rostermatch/<int:rostermatch_id>',views.Delete_rostermatch, name='Delete_rostermatch'),
]