from django.urls import path

from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index') # python manage.py run server. Expect ERROR.
]