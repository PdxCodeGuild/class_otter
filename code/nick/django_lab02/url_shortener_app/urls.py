from django.urls import path
from . import views

app_name = 'url_shortener_app'

urlpatterns = [
    path('', views.short_url,name='short_url'),
    path('<str:short_url>/',views.forward,name='forward')
]
