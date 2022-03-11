from urllib.parse import urlparse
from django.urls import path 

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.BlogListView.as_view(),name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('post/new', views.ChirpCreateView.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.ChirpEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete')

]
