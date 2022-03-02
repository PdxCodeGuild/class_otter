from django.urls import path
from . import views

app_name = 'chirps'
urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.ChirpListView.as_view(), name='home'),
    # path('chirp/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    # path('chirp/hatch/', views.ChirpCreateView.as_view(), name='hatch'),
]