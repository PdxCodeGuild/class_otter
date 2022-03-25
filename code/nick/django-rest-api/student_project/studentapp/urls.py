from django.urls import path
from .views import StudentListView


app_name = 'studentapp'

urlpatterns = [
    path('', StudentListView.as_view(), name='home')
]
