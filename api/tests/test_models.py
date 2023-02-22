from django.test import TestCase

from api.models import Area, Coach, Competition, Player, Team


class AreaModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.area = Area.objects.create(name="England")

    def test_model_content(self):
        self.assertEqual(self.area.name, "England")

    def test_str_repr(self):
        self.assertEqual(str(self.area), "England")


class CompetitionModelTests(TestCase):
    """Test suite for the League competition model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.area = Area.objects.create(name="England")
        cls.competition = Competition.objects.create(
            name="Premier League", code="PL", area=cls.area
        )

    def test_competition_model_creation_is_accurate(self):
        competition = Competition.objects.first()

        self.assertEqual(Competition.objects.count(), 1)
        self.assertEqual(competition.name, self.competition.name)
        self.assertEqual(competition.code, self.competition.code)
        self.assertEqual(competition.area, self.competition.area)

    def test_competition_str_representation(self):
        competition = Competition.objects.first()
        self.assertEqual(str(competition), f"{self.competition.name}")


class TeamModelTests(TestCase):
    """Test suite for the Team model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.area = Area.objects.create(name="England")
        cls.team = Team.objects.create(
            name="Arsenal FC",
            tla="ARS",
            short_name="ARsenal",
            address="75 Drayton Park London",
            area=cls.area,
        )

    def test_team_model_creation_is_accurate(self):
        team = Team.objects.first()

        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(team.name, self.team.name)
        self.assertEqual(team.tla, self.team.tla)
        self.assertEqual(team.short_name, self.team.short_name)
        self.assertEqual(team.address, self.team.address)

    def test_team_str_representation(self):
        team = Team.objects.first()
        self.assertEqual(str(team), f"{self.team.name}")


class PlayerModelTests(TestCase):
    """Test suite for the Player model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.player = Player.objects.create(
            name="David Beckham",
            position="Goalkeeper",
            date_of_birth="1989-12-15",
            nationality="England",
        )

    def test_player_model_creation_is_accurate(self):
        player = Player.objects.first()

        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(player.name, self.player.name)
        self.assertEqual(player.position, self.player.position)
        self.assertEqual(player.date_of_birth, self.player.date_of_birth)
        self.assertEqual(player.nationality, self.player.nationality)

    def test_player_str_representation(self):
        player = Player.objects.first()
        self.assertEqual(str(player), f"{self.player.name}")


class CoachModelTests(TestCase):
    """Test suite for the coach model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.area = Area.objects.create(name="England")
        cls.team = Team.objects.create(
            name="Arsenal FC",
            tla="ARS",
            short_name="ARsenal",
            address="75 Drayton Park London",
            area=cls.area,
        )
        cls.coach = Coach.objects.create(
            name="David Coach",
            date_of_birth="1989-12-15",
            nationality="England",
            team=cls.team,
        )

    def test_coach_model_creation_is_accurate(self):
        coach = Coach.objects.first()

        self.assertEqual(Coach.objects.count(), 1)
        self.assertEqual(coach.name, self.coach.name)
        self.assertEqual(coach.team, self.coach.team)
        self.assertEqual(coach.date_of_birth, self.coach.date_of_birth)
        self.assertEqual(coach.nationality, self.coach.nationality)

    def test_coach_str_representation(self):
        coach = Coach.objects.first()
        self.assertEqual(str(coach), f"{self.coach.name}")
