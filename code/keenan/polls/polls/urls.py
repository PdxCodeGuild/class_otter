from django.urls import path

from . import views

# from for the inputs, we want to take an input (the url path), and state what function to use,
# and then we should give this a name
urlpatterns = [
    path('', views.index, name="index"),
]