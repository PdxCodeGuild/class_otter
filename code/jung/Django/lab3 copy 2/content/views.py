from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed, Reply, Like, BookMark
from uuid import uuid4
from user.models import User
import os
from lab3.settings import MEDIA_ROOT
 
class Main(APIView):
    def get(self, request):

        email = request.session.get('email', None)
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")



        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first() 
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first() 
                reply_list.append(dict(reply_content = reply.reply_content,
                                        nickname=user.nickname
                                        ))
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked= Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            feed_list.append(dict(
                                    id=feed.id,
                                    image=feed.image,
                                    content=feed.content,
                                    like_count=like_count,
                                    profile_image=user.profile_image,
                                    nickname=user.nickname,
                                    reply_list=reply_list,
                                    is_liked = is_liked,
                                ))




        return render(request, "lab3/main.html", context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES['file']
        
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)

        Feed.objects.create(image=image, content=content, email=email, like_count=0)


        return Response(status=200)

class Profile(APIView):
    def get(self, request): 

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, 'content/profile.html', context=dict(user=user))

class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('replay_content', None)

        email = request.session.get('email', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)
        
        return Response(status=200)

class ToggleLike(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        favorite_text = request.data.get('favorite_text', True)
        email = request.session.get('email', None)

        if favorite_text == 'favorite_border':
            is_like = True
        else:
            is_like = False

        like = Like.objects.filter(feed_id=feed_id, email=email).first()

        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id, is_like = is_like, email=email)
        
        return Response(status=200)


class ToggleBookMark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)
        email = request.session.get('email', None)

        if bookmark_text == 'bookmark_border':
            is_marked = True
        else:
            is_marked = False

        bookmark = BookMark.objects.filter(feed_id=feed_id, email=email).first()

        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            BookMark.objects.create(feed_id=feed_id, is_marked = is_marked, email=email)
        
        return Response(status=200)

