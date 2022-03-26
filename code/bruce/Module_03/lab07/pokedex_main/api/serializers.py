from rest_framework import serializers

from pokemon.models import Pokemon, Type


class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back')


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(many=True, source='types')
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'type_detail')

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        model = Type
        fields = ('type', 'pokemon_detail')