from django.urls import path

from .views import (
    CompetitionAPIView,
    CompetitionDetailView,
    PlayersAPIView,
    TeamAPIView,
    import_league,
)

urlpatterns = [
    path("", CompetitionAPIView.as_view(), name="competition_list"),
    path("<int:pk>/", CompetitionDetailView.as_view(), name="competition_detail"),
    path("import-league/<str:code>/", import_league, name="import_league"),
    path("players/", PlayersAPIView.as_view(), name="players_list"),
    path("teams/", TeamAPIView.as_view(), name="team_list"),
]
