from django.urls import path

from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', StudentAPIView.as_view()),
# ]

router = DefaultRouter()
router.register('', StudentViewSet, basename='student')
urlpatterns = router.urls