from django.db import models


class Area(models.Model):
    """
    Represents a particular geographical area or location where league matches are
    being played.
    """

    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Competition(models.Model):
    """
    Also known as a league is an event taking place at an area where many teams participate
    to play matches against each other.
    """

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, related_name="competitions"
    )
    teams = models.ManyToManyField(to="Team", related_name="running_competitions")

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    """
    An ensemble of players also known as squad, a coach which participate in a
    competition or a league.
    """

    name = models.CharField(max_length=250)
    tla = models.CharField(max_length=20)
    short_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="teams")
    squad = models.ManyToManyField(to="Player", related_name="teams")

    def __str__(self):
        return f"{self.name}"


class Player(models.Model):
    """
    A physical sports person who plays the match.
    """

    name = models.CharField(max_length=250)
    position = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=20)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
