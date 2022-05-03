from django.urls import path
from . import views
from students.api.views import api_delete, api_edit , api_new

urlpatterns = [
    path('', views.getRoutes),
    path('students/', views.getStudents),
    path('<slug>/edit/', api_edit, name='edit'),
    path('<slug>/new/', api_new, name='new'),
    path('<slug>/delete/', api_delete, name='delete'),
]
