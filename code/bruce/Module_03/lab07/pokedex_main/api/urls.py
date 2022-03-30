from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('pokemons', views.PokemonViewSet, basename='pokemons')
router.register('types', views.TypeViewSet, basename='types')

urlpatterns = router.urls + [

]
