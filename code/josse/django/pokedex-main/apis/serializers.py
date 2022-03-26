from dataclasses import fields
from django.contrib.auth import get_user_model
from rest_framework import serializers
from pokemon.models import Pokemon, Type

# class PokemonSerializer(serializers.ModelSerializer):
#     model = models.Pokemon
#     field = (

#     )

# class NestedPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = 'Post'
#         fields = ('id', 'number', 'name', 'height', 'weight')

# class NestedUserSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = get_user_model()
#         fields = ('id', 'username')
class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type']


class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(many=True, source='types')
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_detail')


class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        model = Type
        fields = ('type', 'pokemon_detail')


