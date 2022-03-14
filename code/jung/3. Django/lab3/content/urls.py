
from django.urls import path
from .views import ToggleBookMark, UploadFeed, Profile, UploadReply, Main, ToggleLike
urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('profile', Profile.as_view()),
    path('reply', UploadReply.as_view()),
    path('main', Main.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookMark.as_view()),
]
