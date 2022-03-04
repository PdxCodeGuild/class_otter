
# Urls for urlshortener app urlshortener/urls.py
from django.urls import path

from .views import home_view

appname = "urlshortener" #namespacing 

urlpatterns = [
    # Home view
    path("", home_view, name="home")
]   # imports the 'path' function that returns an element to include 
    # in the urlpatterns of the urlshortener app. "name" attribute is 
    # the path's 'namespace.' It can be called inside "templates".
    
