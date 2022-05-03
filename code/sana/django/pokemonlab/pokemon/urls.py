from django.urls import path
from . import views


urlpatterns = [
    path('edit/', views.base_edit, name="edit"),
    path('add/', views.base_add, name="add"),
    path('delete/', views.base_delete, name="delete"),
    # path('<int:number>/', views.pokemon, name="pokemon"),
    # path('api/', views.api_list, name="list"),
    # path('api/', views.api_list, name="lo"),
    # path('<int:number>/api/', views.api_updated, name='updated')
]