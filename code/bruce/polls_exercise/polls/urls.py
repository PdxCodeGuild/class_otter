from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:question_id>/', views.detail, name="detail"),
    # Is 'ResultsView' a required class name?
    # Does 'TheResultsView' work?
    path('<int:pk>/results/', views.TheResultsView.as_view(), name='results'),
    # path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('action/', views.action, name='action'),
    path('add-question/', views.add_question, name='add_question'),
]

