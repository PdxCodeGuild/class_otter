# from django.shortcuts import render
from rest_framework import viewsets, generics, filters

from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from users.models import CustomUser

# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer


# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['type']

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    