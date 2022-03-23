from django.urls import path

from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/', views.PostList.as_view())
]
