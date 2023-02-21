from django.urls import path

from .views import (
    CompetitionAPIView,
    CompetitionDetailView,
    PlayersAPIView,
    TeamAPIView,
    import_league,
    team_players_detail,
)

urlpatterns = [
    path("", CompetitionAPIView.as_view(), name="competition_list"),
    path("<int:pk>/", CompetitionDetailView.as_view(), name="competition_detail"),
    path("import-league/<str:code>/", import_league, name="import_league"),
    path("players/<str:league>/", PlayersAPIView.as_view(), name="players_list_league"),
    path(
        "players/<str:league>/<str:tla>/",
        PlayersAPIView.as_view(),
        name="players_list_league_team",
    ),
    path("teams/<str:tla>/", TeamAPIView.as_view(), name="team_detail"),
    path("teams/<str:tla>/players/", team_players_detail, name="team_players_detail"),
]
