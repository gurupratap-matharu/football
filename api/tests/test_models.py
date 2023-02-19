from django.test import TestCase

from api.models import Area, Competition


class AreaModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.area = Area.objects.create(name="England")

    def test_model_content(self):
        self.assertEqual(self.area.name, "England")

    def test_str_repr(self):
        self.assertEqual(str(self.area), "England")
