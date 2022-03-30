from django.urls import path

from .views import BookAPIView

urlpatterns = [
    # No 'name=' needed since we won't be reversing or hyper-linking.
    path('', BookAPIView.as_view()),
]
