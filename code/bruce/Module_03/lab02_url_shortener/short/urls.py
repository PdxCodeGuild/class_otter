from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>/', views.accept_code_route_to_page, name='accept_code_route_to_page'),
]