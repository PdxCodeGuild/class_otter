from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('short/<str:code>/', views.redirect_to_page, name='redirect_to_page'),
]