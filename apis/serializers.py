from rest_framework import serializers
from pokemon.models import Pokemon, Type
from users.models import CustomUser


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Type
        fields = ('type',)

class NestedPokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(source="types", many=True)
    class Meta:
        model = Pokemon
        fields = (
            'name',
            'image_front',
            'image_back',
            'height',
            'weight',
            'type_detail'
        )

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(many=True, source='types', read_only=True)
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
            'type_detail',
            'types'
        )
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
            "pokemon",
        )
        model = Type

class UserSerializer(serializers.ModelSerializer):
    caught_detail = NestedPokemonSerializer(many=True, read_only=True, source='caught')
    class Meta: 
        model = CustomUser
        fields = (
            'id', 
            'username', 
            'caught', 
            "caught_detail",
        )