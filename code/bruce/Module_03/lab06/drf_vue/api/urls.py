from django import views
from django.urls import path

# This line is here to allow access to api throuth the Django browsable api.
from .views import StudentAPIView

from . import views

urlpatterns = [
    # This path is here to allow access to api through the Django browsable api.
    path('', StudentAPIView.as_view()),

    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('students/', views.StudentList.as_view()),
]
