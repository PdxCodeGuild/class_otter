from django.urls import path

from . import views

app_name = 'glist'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_item, name='create'),
    path('<int:grocery_item_id>/delete/', views.delete_item, name='delete'),
    path('<int:grocery_item_id>/complete/', views.mark_complete, name='complete')

]