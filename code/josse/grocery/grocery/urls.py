from django.urls import path

from . import views
import grocery


app_name = 'grocery'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add_item_to_list, name='create'),
    path('mark_complete/<int:item_id>', views.mark_complete, name='mark_complete')
#     path('<int:pk>/delete', views.delete, name='delete')
]
