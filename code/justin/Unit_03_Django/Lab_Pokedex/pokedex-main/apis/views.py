from rest_framework import viewsets
from pokemon import models as pokemonModels
from users import models as userModels
from .serializers import PokemonSerializer, TypeSerializer, CustomUserSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = pokemonModels.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = pokemonModels.Type.objects.all()
    serializer_class = TypeSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = userModels.CustomUser.objects.all()
    serializer_class = CustomUserSerializer
