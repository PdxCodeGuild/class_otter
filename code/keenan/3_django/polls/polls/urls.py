from django.urls import path

from . import views

# from for the inputs, we want to take an input (the url path), and state what function to use,
# and then we should give this a name

app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]

# http://127.0.0.1:8000/polls/1/vote/