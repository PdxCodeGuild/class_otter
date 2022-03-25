from django import views
from django.urls import path

# from .views import StudentAPIView
from . import views

urlpatterns = [
    # path('', StudentAPIView.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('students/', views.StudentList.as_view()),
]
