from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.DetailStudent.as_view()),
    path('', views.ListStudent.as_view()),
]
