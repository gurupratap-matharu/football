"""Script that holds all the business logic needed to talk to the football API"""

import logging

from django.conf import settings

import requests

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

        competition_data = self.get_competition_from_api()
        teams_data = self.get_teams_from_api().get("teams")

        teams = []
        for data in teams_data:
            team = self.create_team(data=data)

            squad = data["squad"]

            if squad:
                # Squad found in api so build them and create m2m link
                players = self.create_players(squad=data["squad"])
                team.squad.add(*players)

            else:
                # No squad so build the coach even if null
                _ = self.create_coach(coach=data["coach"], team=team)

            teams.append(team)

        competition = self.create_competition(data=competition_data)
        competition.teams.add(*teams)

    def hit_api(self, url):
        """
        Helper method to hit the football API at any desired endpoint.
        """

        logger.info("hitting (🚀) %s..." % url)

        try:
            response = requests.get(url=url, headers=self.HEADERS)
            response.raise_for_status()

        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        except requests.exceptions.Timeout as e:
            raise Exception("The url timed out", e)

        except requests.exceptions.TooManyRedirects as e:
            raise Exception("The url led to too many redirects!", e)

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        else:
            return response.json()

    def get_competition_from_api(self):
        """
        Hits the football API at the competition endpoint and parses the json data.
        """

        url = self.URI + f"competitions/{self.league}"
        return self.hit_api(url=url)

    def get_teams_from_api(self):
        """
        Hits the football API at the teams endpoint and parses the json data.
        """

        url = self.URI + f"competitions/{self.league}/teams"
        return self.hit_api(url=url)

    def create_area(self, area):
        """
        Get or create an area.
        """

        a, created = Area.objects.get_or_create(name=area["name"], code=area["code"])

        if created:
            logger.info("created area(🌍): %s" % a)
        else:
            logger.info("already exists area(🌍): %s" % a)

        return a

    def create_competition(self, data):
        """
        Get or create a league in the database.
        """
        c, created = Competition.objects.get_or_create(
            name=data["name"],
            code=data["code"],
            area=self.create_area(area=data["area"]),
        )

        if created:
            logger.info("created league(🥅):%s" % c)
        else:
            logger.info("already exists league(🥅):%s" % c)

        return c

    def create_team(self, data):
        """
        Get or create a single team in the database.
        """

        team, created = Team.objects.get_or_create(
            name=data["name"],
            tla=data["tla"],
            short_name=data["shortName"],
            address=data["address"],
            area=self.create_area(area=data["area"]),
        )

        if created:
            logger.info("created team(👯‍♀️):%s" % team)
        else:
            logger.info("already exists team(👯‍♀️):%s" % team)

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

        c, created = Coach.objects.get_or_create(
            name=coach["name"],
            date_of_birth=coach["dateOfBirth"],
            nationality=coach["nationality"],
            team=team,
        )

        if created:
            logger.info("created coach(👮‍♀️):%s" % c)
        else:
            logger.info("already exists coach(👮‍♀️):%s" % c)

        return c

    def __repr__(self):
        return f"{self.league}"
