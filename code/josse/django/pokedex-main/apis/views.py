from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type 
from .serializers import PokemonSerializer, TypeSerializer
from apis import serializers


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
