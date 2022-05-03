
from pokemon.models import Pokemon, Type
# from .serializers import PokemonSerializer, TypesSerializer , CustomUserSerializer
from api.serializers import PokemonSerializer, TypesSerializer
from rest_framework import generics, viewsets
# from django.contrib.auth import get_user_model
# # from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.http import HttpResponseNotFound
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import action

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    # @action(methods=['POST'])
    
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         pokemon = Pokemon.objects.get(pk=pk)
#     except Pokemon.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PokemonSerializer(pokemon)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PokemonSerializer(pokemon, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         pokemon.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = CustomUserSerializer

# class CustomUserView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CustomUserSerializer
#     def get_object(self):
#         return self.request.user




# @api_view(['PUT'])
# def api_edit(request, slug):

#     try:
#         pokemon = Pokemon.objects.get(slug=slug)
#     except Pokemon.DoesNotExist:
#         return Response(status=HttpResponseNotFound)
#     if request.method == 'PUT':
#         serializer = PokemonSerializer(pokemon, data=request.data)
#         data= {}
#         if serializer.is_valid():
#             serializer.save()
#             data["success"] = "edit successful"
#             return Response(data=data)

#         return Response(serializer.data)

# @api_view(['DELETE'])
# def api_delete(request, slug):

#     try:
#         pokemon = Pokemon.objects.get(slug=slug)
#     except Pokemon.DoesNotExist:
#         return Response(status=HttpResponseNotFound)
#     if request.method == 'DELETE':
#         operation = pokemon.delete()
#         data= {}
#         if operation:
#             data["sucess"] = "deletion successful"
#         else:
#             data["failure"] = "deletion failure"
#         return Response(data=data)

# @api_view(['POST'])
# def api_new(request, slug):
#     pokemon = Pokemon.objects.create()
#     if request.method == 'POST':
#         serializer = PokemonSerializer(pokemon, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)






















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