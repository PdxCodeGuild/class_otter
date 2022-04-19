from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from pokemon import models as pokemonModels
from users import models as userModels
from .serializers import PokemonSerializer, TypeSerializer, CustomUserSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = pokemonModels.Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=True, methods=['put'])
    def capture(self, request, pk=None):
        caught_by_id = request.data['userID']
        pokemon = self.get_object()

        pokemon.caught_by.add(caught_by_id)
        pokemon.save()
        responseObject = {'caught_by': f'{pokemon.caught_by}'}

        return Response(responseObject)

    @action(detail=True, methods=['put'])
    def release(self, request, pk=None):
        caught_by_id = request.data['userID']
        pokemon = self.get_object()
        
        pokemon.caught_by.remove(caught_by_id)
        pokemon.save()
        responseObject = {'caught_by': f'{pokemon.caught_by}'}

        return Response(responseObject)

class TypeViewSet(viewsets.ModelViewSet):
    queryset = pokemonModels.Type.objects.all()
    serializer_class = TypeSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = userModels.CustomUser.objects.all()
    serializer_class = CustomUserSerializer
