from rest_framework import serializers

from api.models import Coach, Competition, Player, Team


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ("name", "code")


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("name", "position", "date_of_birth", "nationality")


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ("name", "date_of_birth", "nationality")


class TeamSquadSerializer(serializers.ModelSerializer):
    squad = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("id", "tla", "short_name", "name", "address", "squad")


class TeamCoachSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("id", "tla", "short_name", "name", "address", "coach")


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "tla", "short_name", "name", "address")
