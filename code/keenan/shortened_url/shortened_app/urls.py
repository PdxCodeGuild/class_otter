# shortened_app urls

from django.urls import path
from . import views

app_name = 'shortened_app'
urlpatterns = [
    path('', views.index, name='index')

]