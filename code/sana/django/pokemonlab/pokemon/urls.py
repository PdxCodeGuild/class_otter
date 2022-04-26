from django.urls import path
from . import views


urlpatterns = [
    path('', views.edit, name="edit"),
    # path('<int:number>/', views.pokemon, name="pokemon"),
    # path('api/', views.api_list, name="list"),
    # path('api/', views.api_list, name="lo"),
    # path('<int:number>/api/', views.api_updated, name='updated')
]