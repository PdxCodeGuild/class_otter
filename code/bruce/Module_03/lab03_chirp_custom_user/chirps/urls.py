from django.urls import path

from . import views

app_name = 'chirps'
urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('<int:pk>', views.ChirpDetailView.as_view(), name='detail'),
    path('hatch/', views.ChirpCreateView.as_view(), name='hatch'),
    path('<int:pk>/moderate/', views.ChirpModerateView.as_view(), name='moderate'),
    path('<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),
]
