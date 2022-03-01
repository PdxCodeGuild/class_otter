from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:pk>/', views.index),
    # path('<int:pk>/', views.index, name='index'),
    # path('uncomplete/<int:pk>/', views.uncomplete, name='uncomplete'),

    path('cards/', views.index_cards, name='index_cards'), # <int:pk>/
    path('cards/<int:pk>/', views.index_cards),
    # path('wide/', views.index_wide, name='index_wide'),
    path('add/', views.add, name='add'),
    path('short/<str:code>/', views.redirect_to_page, name='redirect_to_page'),
]