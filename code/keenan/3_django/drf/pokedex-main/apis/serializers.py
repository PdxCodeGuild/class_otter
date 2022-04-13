from rest_framework import serializers

from pokemon import models

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',

        )
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'type',
        )
        model = models.Type