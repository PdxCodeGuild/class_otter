from rest_framework import serializers
from pokemon import models


class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(many=True)
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
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer(many=True)
    class Meta:
        fields = [
            'id',
            'type',
            'pokemon'
        ]
        model = models.Type