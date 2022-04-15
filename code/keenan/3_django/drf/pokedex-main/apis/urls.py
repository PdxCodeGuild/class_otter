from django.urls import path

from .views import PokemonViewSet, TypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')

urlpatterns = router.urls