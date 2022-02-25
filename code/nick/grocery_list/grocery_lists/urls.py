from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'grocery'
grocery_lists = 'grocery_lists'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('new/', views.new, name='new')
]
