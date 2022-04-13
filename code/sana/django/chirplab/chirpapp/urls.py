from django.urls import path
from . import views
from .views import ChirpListView, ChirpPostView

urlpatterns = [
    path('', ChirpListView.as_view(), name='home'),
    path('chirp/', views.postchirp, name='chirp'),
]
