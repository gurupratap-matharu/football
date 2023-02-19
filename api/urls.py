from django.urls import path

from .views import CompetitionAPIView

urlpatterns = [
    path("", CompetitionAPIView.as_view(), name="competition_list"),
]
