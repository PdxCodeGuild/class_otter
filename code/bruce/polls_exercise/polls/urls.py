from django.urls import path

from . import views

# Now, using generic views:
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Need to use primary key 'pk' since we are using the automagical awesomeness that is Django.
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # We still use 'question_id' here since we are doing the logic.
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name="index"),
#     # Use path() and variables.
#     # This 'question_id' matches 'question_id' from view functions above.
#     # These path()'s are passing 'question_id' on to the view function.
#     path('<int:question_id>/', views.detail, name="detail"),
#     path('<int:question_id>/results/', views.results, name="results"),
#     path('<int:question_id>/vote/', views.vote, name="vote"),
# ]

