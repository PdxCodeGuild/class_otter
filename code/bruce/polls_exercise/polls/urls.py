from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # Use path() and variables.
    # This 'question_id' matches 'question_id' from view functions above.
    # These path()'s are passing 'question_id' on to the view function.
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
