"""Script that holds all the business logic needed to talk to the football API"""

import json
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class APIService:
    """
    Our custom service that encapsulates all the logic needed to talk to the
    football api.
    """

    URI = settings.FOOTBALL_API_URL
    HEADERS = {"X-Auth-Token": settings.FOOTBALL_API_TOKEN}

    def __init__(self, league=None):
        self.league = league

    def run(self):
        logger.info("running api service 🚨...")

        response = requests.get(self.URI, headers=self.HEADERS)
        for match in response.json()["matches"]:
            print(match)

    def __repr__(self):
        return f"{self.league}"
