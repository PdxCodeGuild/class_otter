from django.urls import path

from .views import PokemonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokemons', PokemonViewSet, basename='pokemons')
router.register('types')
urlpatterns = router.urls