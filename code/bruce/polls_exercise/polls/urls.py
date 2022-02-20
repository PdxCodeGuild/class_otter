from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:question_id>/', views.detail, name="detail"),
    path('<int:pk>/results/', views.TheResultsView.as_view(), name='results'),
    # path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add/', views.add, name='add'),
    path('add-question/', views.add_question, name='add_question'),
    path('delete/', views.DeleteView.as_view(), name='delete'),
    # path('<int:question_id>/delete-question/', views.delete_single_question, name='delete_single_question'),
    path('delete-question/', views.delete_single_question, name='delete_single_question'),
    path('delete-multiple-questions/', views.delete_multiple_questions, name='delete_multiple_questions'),
]

