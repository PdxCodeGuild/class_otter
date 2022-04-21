from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('pokemon/', views.Pokemon_View_Sets),
    path('users/', views.CustomUser_View),
    path('user/', views.Type_View_Sets),
]