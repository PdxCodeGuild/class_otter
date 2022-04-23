
from unicodedata import name
from rest_framework.serializers import ModelSerializer

from pokemon.models import Pokemon, Type
from django.contrib.auth import get_user_model

# from base.models import Room


class NestedPokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name',)


class NestedTypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class PokemonSerializer(ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types', read_only=True)
    class Meta:
        fields = ('id', 'name', 'number', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'type_info' )
        model = Pokemon

class TypesSerializer(ModelSerializer):
    pokemon_info = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        model = Type
        fields = ('type', 'pokemon_info')

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('caught', 'id', 'username')






















# class TypeSerializer(serializers.Serializer):
#     type = serializers.CharField(max_length=50)
#     pokemon = serializers.ManyToManyField(Pokemon, related_name='types')

# class PokemonSerializer(serializers.Serializer):
#     number = serializers.IntegerField()
#     name = serializers.CharField(max_length=200)
#     height = serializers.FloatField()
#     weight = serializers.FloatField()
#     image_front = serializers.URLField()
#     image_back = serializers.URLField()
#     caught_by = serializers.ManyToManyField(get_user_model(), related_name='caught')