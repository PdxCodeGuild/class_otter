
from pokemon.models import Pokemon, Type
# from .serializers import PokemonSerializer, TypesSerializer , CustomUserSerializer
from api.serializers import PokemonSerializer, TypesSerializer
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
# from django.http import JsonResponse

class PokemonViewSet(viewsets.ModelViewSet):

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = CustomUserSerializer

# class CustomUserView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CustomUserSerializer
#     def get_object(self):
#         return self.request.user



























# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/pokemon',
#         'GET /api/pokemon/:id'
#     ]
#     return JsonResponse(routes, safe=False)

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/pokemon',
#         'GET /api/pokemons',
#         'GET /api/types',
#         'GET /api/type/:type',
#         'GET /api/pokemon/:name',
#     ]
#     return Response(routes)


# @api_view(['GET'])
# def getPokemons(request):
#     pokemons = Pokemon.objects.all()
#     serializer = PokemonSerializer(pokemons, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getPokemon(request, pk):
#     pokemon = Pokemon.objects.get(name=pk)
#     serializer = PokemonSerializer(pokemon, many=False)
#     return Response(serializer.data)



# @api_view(['GET'])
# def getTypes(request):
#     rooms = Type.objects.all()
#     serializer = TypeSerializer(rooms, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getType(request, pk):
#     type = Type.objects.get(type=pk)
#     serializer = TypeSerializer(type, many=False)
#     return Response(serializer.data)