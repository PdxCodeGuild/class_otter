from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models import Post

class NestedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = get_user_model()
        # I removed author 'id' since it is shown in post 'author' and there is only one 'author' per 'post'.
        # fields = ('id', 'username')
        fields = ('username',)

class PostSerializer(serializers.ModelSerializer):
    # 'author' is a 'Post' attribute.
    author_detail = NestedUserSerializer(read_only=True, source='author')
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'author_detail', 'created', 'updated', 'body')

class UserSerializer(serializers.ModelSerializer):
        # Where does 'posts' come frome? # 'related_name="posts"' in 'posts.models.Post.author'? 'posts' is the 'related_name'.
    posts_detail = NestedPostSerializer(many=True, read_only=True, source='posts')
    # 'read_only=True' is needed since a 'user' could have multiple 'post's.
    class Meta: 
        model = get_user_model()
        # 'posts' was providing an array of post ids, now (from above) it will provide array of actual post objects.
        fields = ('id', 'username', 'posts', 'posts_detail')