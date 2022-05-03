from email.mime import base
from django.urls import path
from .views import CustomUserViewSet, PokemonViewSet, TypeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')
router.register('profiles', CustomUserViewSet, basename='profiles')
urlpatterns = router.urls