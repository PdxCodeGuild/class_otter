from rest_framework import generics

from pokemon import models
from .serializers import PokemonSerializer, TypeSerializer

class PokemonList(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeList(generics.ListCreateAPIView):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Type.objects.all()
    serializer_class = TypeSerializer
