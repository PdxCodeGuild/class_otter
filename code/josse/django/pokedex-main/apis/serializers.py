from dataclasses import fields
from django.contrib.auth import get_user_model
from rest_framework import serializers
from pokemon.models import Pokemon, Type


class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type']


class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(many=True, source='types', read_only=True)
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_detail', 'id')


class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='pokemon', read_only=True)
    class Meta:
        model = Type
        fields = ('type', 'pokemon_detail')

