from django.urls import path

from .views import ListStudent, DetailStudent

urlpatterns = [
    path('', ListStudent.as_view()),
    path('<int:pk>/', DetailStudent.as_view()),
]