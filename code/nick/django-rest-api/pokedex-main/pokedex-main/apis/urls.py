from django.db import router
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PokemonList.as_view()),
    path('<int:pk>/', views.PokemonDetail.as_view()),
    path('type/', views.TypeList.as_view()),
    path('type/<int:pk>/', views.TypeDetail.as_view()),
    
]

