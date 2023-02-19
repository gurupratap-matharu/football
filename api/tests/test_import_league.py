from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ImportLeagueAPITests(APITestCase):
    """
    Suite to test Importing of league data from football api.
    """

    def test_api_list_view(self):
        response = self.client.get(reverse("import_league", args=["PL"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
