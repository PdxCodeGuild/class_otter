
from django.urls import path
from .views import UploadFeed

urlpatterns = [
    path('upload', UploadFeed.as_view())
]
