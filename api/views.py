from rest_framework import generics

from .models import Competition
from .serializers import CompetitionSerializer


class CompetitionAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
