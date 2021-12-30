from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet, CurrentUserView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]


# from .views import PostList, PostDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]
