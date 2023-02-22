from django.db import models


class Area(models.Model):
    """
    Represents a particular geographical area or location where league matches are
    being played.
    """

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Competition(models.Model):
    """
    Also known as a league is an event taking place at an area where many teams participate
    to play matches against each other.
    """

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10, unique=True)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, null=True, related_name="competitions"
    )
    teams = models.ManyToManyField(
        to="Team", blank=True, related_name="running_competitions"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    """
    An ensemble of players also known as squad, a coach which participate in a
    competition or a league.
    """

    name = models.CharField(max_length=250, blank=True, null=True)
    tla = models.CharField(max_length=20, unique=True, blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, related_name="teams", null=True
    )
    squad = models.ManyToManyField(
        to="Player", blank=True, related_name="current_teams"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Player(models.Model):
    """
    A physical sports person who plays the match.
    """

    name = models.CharField(max_length=250, unique=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Coach(models.Model):
    """
    A coach for a team.
    """

    name = models.CharField(max_length=250, blank=True, null=True, unique=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    team = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="coach", null=True
    )

    def __str__(self):
        return f"{self.name}"
