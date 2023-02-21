from rest_framework import serializers

from api.models import Competition, Player, Team


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ("name", "code")


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ("name", "position", "date_of_birth", "nationality")


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ("name", "tla", "short_name", "address")
