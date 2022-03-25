from django.urls import path
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls