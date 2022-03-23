
# Urls for urlshortener app urlshortener/urls.py
from django.urls import path

from .views import home_view, redirect_url_view

appname = "urlshortener" #namespacing 

urlpatterns = [
    # Home view
    path('', home_view, name='home'), 
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]
    
