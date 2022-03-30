from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer
from .permissions import IsLoggedInOrReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsLoggedInOrReadOnly]

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    