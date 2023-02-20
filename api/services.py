"""Script that holds all the business logic needed to talk to the football API"""

import json
import logging
import pdb

import requests
from django.conf import settings

from .models import Area, Coach, Competition, Player, Team

logger = logging.getLogger(__name__)


class APIService:
    """
    Our custom service that encapsulates all the logic needed to talk to the
    football api.
    """

    URI = settings.FOOTBALL_API_BASE_URL
    HEADERS = {"X-Auth-Token": settings.FOOTBALL_API_TOKEN}

    def __init__(self, league=None):
        self.league = league

    def run(self):
        logger.info("running api service 🚨...")

        url = self.URI + f"competitions/{self.league}/teams"
        logger.info("hitting (🚀) %s..." % url)

        with open("api/samples/teams.json", "r") as f:
            response = json.load(f)

        competition_data = response.get("competition")
        teams_data = response.get("teams")

        teams = []
        for data in teams_data:
            team = self.create_team(data=data)
            _ = self.create_coach(coach=data["coach"], team=team)
            players = self.create_players(squad=data["squad"])
            team.squad.add(*players)
            teams.append(team)

        competition = self.create_competition(data=competition_data)
        competition.teams.add(*teams)
        # response = requests.get(self.URI, headers=self.HEADERS)

    def create_area(self, area):
        """
        Get or create an area.
        """

        a, _ = Area.objects.get_or_create(name=area["name"], code=area["code"])
        logger.info("created area(🌍): %s" % a)

        return a

    def create_competition(self, data):
        """
        Get or create a league in the database.
        """

        c, _ = Competition.objects.get_or_create(name=data["name"], code=data["code"])

        logger.info("created league(🥅):%s" % c)

        return c

    def create_team(self, data):
        """
        Get or create a single team in the database.
        """

        team, _ = Team.objects.get_or_create(
            name=data["name"],
            tla=data["tla"],
            short_name=data["shortName"],
            address=data["address"],
            area=self.create_area(area=data["area"]),
        )

        logger.info("created team(👯‍♀️):%s" % team)

        return team

    def create_players(self, squad):
        """
        Bulk create players in one go from a list of dicts.
        """

        players = [
            Player.objects.get_or_create(
                name=p["name"],
                position=p["position"],
                date_of_birth=p["dateOfBirth"],
                nationality=p["nationality"],
            )
            for p in squad
        ]
        players = [x[0] for x in players]

        logger.info("created players(⚽️): %s" % len(players))

        return players

    def create_coach(self, coach, team):
        """
        Create a single coach for a team.
        """

        c, _ = Coach.objects.get_or_create(
            name=coach["name"],
            date_of_birth=coach["dateOfBirth"],
            nationality=coach["nationality"],
            team=team,
        )

        logger.info("created coach(👮‍♀️):%s" % c)

        return c

    def __repr__(self):
        return f"{self.league}"
