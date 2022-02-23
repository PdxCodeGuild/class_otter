from django.urls import path
from . import views

app_name = 'GroceryList'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('<int:item_id>/update/', views.update, name='update'),
    path('<int:item_id>/delete/', views.delete, name='delete'),
]