# A 'permissions' from 'rest_framework':
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

# If we want to do something with defualt user model:
# from django.contrib.auth.models import User

# Or, for our own CustomUser:
# from users.models import CustomUser

from posts.models import Post
from .serializers import PostSerializer, UserSerializer
# A 'permissions' which we defined.
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Our 'permissions.IsAuthorOrReadOnly':
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # Django's 'permissions.IsAuthenticatedOrReadOnly':
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


# ############################################################
# # View which doesn't require pk for specific Post.
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# # View which does require pk for specific Post.
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# ############################################################

