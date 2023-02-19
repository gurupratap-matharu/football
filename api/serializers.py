from rest_framework import serializers

from api.models import Competition


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ("name", "code")
