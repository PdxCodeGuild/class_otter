from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/', views.PostList.as_view(), name='post_detail'),
    # path('post/new/', views.PostCreateView.as_view(), name='new'),
    # path('post/delete/', views.PostDeleteView.as_view(), name='delete'),
]
