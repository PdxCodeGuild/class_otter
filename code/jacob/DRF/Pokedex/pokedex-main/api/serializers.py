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
    type_detail = NestedTypeSerializer(read_only=True, many=True, source="types")
    class Meta:
        model = models.Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'types', 'type_detail', 'id')

class TypeSerializer(serializers.ModelSerializer):
    pokemon = NestedNameSerializer(read_only=True, many=True)
    class Meta:
        model = models.Type
        fields = ('type', 'pokemon', 'id')