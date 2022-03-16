
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/<str:slink>', views.goto, name='exit' )
]


#shortenr url local/abcdf {unique_url/short} 