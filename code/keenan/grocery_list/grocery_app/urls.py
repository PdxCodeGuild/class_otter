# grocery_app URLs

from django.urls import path
from . import views


app_name = 'grocery_list'
urlpatterns = [
    # these names need to match the redirects, this may be why my list / index page is broken
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    # path('complete/<int:pk>/', views.complete, name='complete')
]