
from django.urls import path
from . import views

urlpatterns = [
    path('', views.process, name='index'),
    path('<str:pk>', views.goto, name='exit' )
]


#shortenr url local/abcdf {unique_url/short} 