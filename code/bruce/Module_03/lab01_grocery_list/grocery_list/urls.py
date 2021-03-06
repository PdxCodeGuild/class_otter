from django.urls import path

from . import views

# TODO: Figure out the source of 'app_name'.
# It may be from app/apps.py/GroceryListConfig().name.
app_name = 'grocery_list'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    # path('complete/', views.complete, name='complete'),
    # path('uncomplete/', views.uncomplete, name='uncomplete'),
    # path('delete/', views.delete, name='delete'),
    path('uncomplete/<int:pk>/', views.uncomplete, name='uncomplete'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]