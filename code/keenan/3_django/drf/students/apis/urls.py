from django.urls import path
# this liststudent and detailstudent might be redundant to the todoviewset below
# from .views import ListStudent, DetailStudent

# 
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

# this is the apis views.py

# urlpatterns = [
#     path('', ListStudent.as_view()),
#     path('<int:pk>/', DetailStudent.as_view()),
# ]

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls