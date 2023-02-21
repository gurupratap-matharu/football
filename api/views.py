import logging

from django.core.management import call_command
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Competition, Player, Team
from .serializers import CompetitionSerializer, PlayerSerializer, TeamSerializer

logger = logging.getLogger(__name__)


@csrf_exempt
def import_league(request, code=None):
    """Loads league data into the database"""

    call_command("load_league_data", league=code)
    return JsonResponse({"status": "All data imported!"})


class CompetitionAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetailView(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class PlayersAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
