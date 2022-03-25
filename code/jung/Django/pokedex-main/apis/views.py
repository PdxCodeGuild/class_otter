# from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import 

from pokemon import models
from pokemon.models import Pokemon
from .serializers import PokemonSerializer, TypeSerializer

# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer


# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = TypeSerializer

    