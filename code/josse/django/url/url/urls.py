from django.urls import path

from . import views

app_name = 'url'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-link/<str:code>/', views.redirect_to_page, name='redirect_to_page'),
]
