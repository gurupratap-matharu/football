from django.urls import path

from .views import CompetitionAPIView, CompetitionDetailView, import_league

urlpatterns = [
    path("", CompetitionAPIView.as_view(), name="competition_list"),
    path("<int:pk>/", CompetitionDetailView.as_view(), name="competition_detail"),
    path("import-league/<str:code>/", import_league, name="import_league"),
]
