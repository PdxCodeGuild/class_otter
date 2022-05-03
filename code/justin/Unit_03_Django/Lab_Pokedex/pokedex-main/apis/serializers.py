from rest_framework import serializers
from pokemon import models as pokemonModels
from users import models as userModels


class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True)
    caught_by = serializers.StringRelatedField(many=True)
    class Meta:
        fields = [
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'types'
        ]
        model = pokemonModels.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer(many=True)
    class Meta:
        fields = [
            'id',
            'type',
            'pokemon'
        ]
        model = pokemonModels.Type

class CustomUserSerializer(serializers.ModelSerializer):
    caught = PokemonSerializer(many=True)
    class Meta:
        fields = [
            'id',
            'username',
            'email',
            'caught'
        ]
        model = userModels.CustomUser