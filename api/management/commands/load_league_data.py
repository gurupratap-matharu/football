"""A utility script to load league data into the db for the Football api.

Running this script would populate the following db models
    - Competitions (Leagues)
    - Teams
    - Players
    - Coaches

with fresh data fetched from the API
"""


from django.core.management.base import BaseCommand

from api.models import Coach, Competition, Player, Team
from api.services import APIService


class Command(BaseCommand):
    """
    Management command which populates database with Football API data
    """

    help = "Fetch league data from the API and populate the database"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "-l",
            "--league",
            type=str,
            help="The league for which the data is to be fetched.",
        )

    def success(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))

    def danger(self, msg):
        self.stdout.write(self.style.HTTP_BAD_REQUEST(msg))

    def handle(self, *args, **kwargs):
        league = kwargs.get("league")

        self.success("League: %s" % league)
        self.success("Fetching data from api 📡...")

        _ = APIService(league=league).run()

        self.success(
            f"""
        Competitions : {Competition.objects.count()}
        Teams        : {Team.objects.count()}
        Players      : {Player.objects.count()}
        Coach        : {Coach.objects.count()}"""
        )

        self.success("All done! 💖💫✅")
