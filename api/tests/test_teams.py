from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Area, Competition, Player, Team


class TeamsAPITests(APITestCase):
    """
    Suite to test Teams API endpoints."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Build mock data here to use for the entire test suite."""

        cls.area = Area.objects.create(name="England")
        cls.competition = Competition.objects.create(
            name="Premier League", code="PL", area=cls.area
        )
        cls.bou = Team.objects.create(
            name="AFC Bournemouth",
            tla="BOU",
            short_name="Bournemouth",
            address="Dean Court, Kings Park Bournemouth BH7 7AF",
            area=cls.area,
        )
        cls.ars = Team.objects.create(
            name="Arsenal FC",
            tla="ARS",
            short_name="Arsenal",
            address="75 Drayton Park London N5 1BU",
            area=cls.area,
        )
        cls.competition.teams.add(cls.bou, cls.ars)

        cls.aaron = Player.objects.create(
            name="Aaron Ramsdale",
            position="Goalkeeper",
            date_of_birth="1998-05-14",
            nationality="England",
        )
        cls.ben = Player.objects.create(
            name="Ben White",
            position="Defence",
            date_of_birth="1997-10-08",
            nationality="England",
        )
        cls.bou.squad.add(cls.aaron, cls.ben)
        # we don't add any players to ars team

    def test_team_detail_api_view(self):
        response = self.client.get(reverse("team_detail", args=["BOU"]), format="json")

        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "BOU")
        self.assertContains(response, "Bournemouth")

    def test_team_detail_api_view_with_players_shows_the_squad(self):
        response = self.client.get(reverse(), format="json")
