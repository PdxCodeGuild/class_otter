from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('shrt.<str:short_code>/', views.link_through, name='link_through'),
]