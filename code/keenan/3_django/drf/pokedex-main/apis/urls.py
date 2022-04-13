from django.urls import path

from .views import ListPokemon, ListType

urlpatterns = [
    path('', ListPokemon.as_view()),
    path('<int:pk>/', ListType.as_view()),
]