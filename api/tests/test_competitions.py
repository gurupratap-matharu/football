from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Area, Competition


class CompetitionAPITests(APITestCase):
    """
    Suite to test Competition(league) api endpoints.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        """Build mock data here to use for the entire test suite"""

        cls.area = Area.objects.create(name="England")
        cls.competition = Competition.objects.create(
            name="Premier League", code="PL", area=cls.area
        )

    def test_api_list_view(self):
        response = self.client.get(reverse("competition_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Competition.objects.count(), 1)
        self.assertContains(response, self.competition)
