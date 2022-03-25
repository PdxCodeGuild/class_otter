from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view())
]

# urlpatterns = [
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('posts/', views.PostList.as_view())
# ]
