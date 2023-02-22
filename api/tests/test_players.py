from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Area, Competition, Player, Team


class PlayerAPITests(APITestCase):
    """
    Suite to test Player API endpoints.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """Build mock data here to use for the entire test suite."""

        cls.area = Area.objects.create(name="England")
        cls.competition = Competition.objects.create(
            name="Premier League", code="PL", area=cls.area
        )
        # create two teams
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

        # create two players and add one player to each team
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
        cls.bou.squad.add(cls.aaron)
        cls.ars.squad.add(cls.ben)
        # competition has both players
        # each team has only one player

    def test_players_list_api_view_with_league_code(self):
        response = self.client.get(
            reverse("players_list_league", args=["PL"]), format="json"
        )

        self.assertEqual(Player.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Ben White")
        self.assertContains(response, "Aaron Ramsdale")

    def test_players_list_api_view_with_league_code_and_team_code(self):
        """
        Here we request for the league but for only one team.
        so we should get only one player in response
        """

        response = self.client.get(
            reverse("players_list_league_team", kwargs={"league": "PL", "tla": "ARS"}),
            format="json",
        )

        self.assertEqual(Player.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Ben White")
        self.assertNotContains(
            response, "Aaron Ramsdale"
        )  # <-- make sure aaron is not part of response

    def test_players_list_api_view_with_league_code_and_team_code_for_second_team(self):
        """
        Here we request for the league but for only one team.
        so we should get only one player in response
        """

        response = self.client.get(
            reverse("players_list_league_team", kwargs={"league": "PL", "tla": "BOU"}),
            format="json",
        )

        self.assertEqual(Player.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Aaron Ramsdale")
        self.assertNotContains(
            response, "Ben White"
        )  # <-- make sure Ben is not part of response
