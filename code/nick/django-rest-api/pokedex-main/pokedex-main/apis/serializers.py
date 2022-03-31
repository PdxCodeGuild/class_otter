from dataclasses import field, fields
from rest_framework import serializers
from pokemon import models

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = ('type',)

class NestedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ('name',)

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "number",
            "name",
            "height",
            "weight",
            "image_front",
            "image_back",
            "types"
        )
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    pokemon = NestedNameSerializer(read_only=True, many=True)
    class Meta:
        model = models.Type
        fields = ('type', 'pokemon', 'id')