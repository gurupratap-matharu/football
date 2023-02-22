import logging

from django.core.management import call_command
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from .models import Competition, Player, Team
from .serializers import (
    CompetitionSerializer,
    PlayerSerializer,
    TeamCoachSerializer,
    TeamSerializer,
    TeamSquadSerializer,
)

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
    serializer_class = PlayerSerializer

    def get_queryset(self):
        """
        Filter the players queryset for a league (or team as well but optional)as
        determined by the league / tla portion of the URL.

        Note:
            - to filter by league we use the league code in the URL
            - to filter by team we use its TLA code in the URL
        """

        league_code = self.kwargs.get("league")
        tla = self.kwargs.get("tla")

        league = get_object_or_404(Competition, code__icontains=league_code)

        logger.info("filtering players for league:%s" % league)

        teams = league.teams.all()

        if tla:
            _ = get_object_or_404(Team, tla__iexact=tla)
            teams = teams.filter(tla__iexact=tla)
            logger.info("filtering players for teams(👫):%s" % teams)

        return Player.objects.filter(current_teams__in=teams)


class TeamAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    team_squad_serializer_class = TeamSquadSerializer
    team_coach_serializer_class = TeamCoachSerializer

    def get_object(self):
        queryset = self.get_queryset()
        tla = self.kwargs["tla"]
        return get_object_or_404(queryset, tla__iexact=tla)

    def get_serializer_class(self):
        """
        Determins which serializer to user `Team` or `TeamWithSquad`
        """

        show_players = self.request.query_params.get("players")  # type:ignore
        team = self.get_object()

        if show_players and team.squad.exists():
            logger.info("team:%s has a squad so showing it..." % team)

            if hasattr(self, "team_squad_serializer_class"):
                return self.team_squad_serializer_class

        else:
            logger.info("team:%s has no squad so showing only coach..." % team)

            if hasattr(self, "team_coach_serializer_class"):
                return self.team_coach_serializer_class

        return super().get_serializer_class()


def team_players_detail(request, tla=None):
    url = reverse("team_detail", args=[tla]) + "?players=True"

    logger.info("team_players_detail: tla:%s" % tla)
    logger.info("redirecting to: %s" % url)

    return redirect(url)
