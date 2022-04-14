from rest_framework import viewsets
from pokemon import models
from .serializers import PokemonSerializer, TypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer
