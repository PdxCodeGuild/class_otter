from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')
router.register('type', views.TypeViewSet, basename='type')
# router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls 