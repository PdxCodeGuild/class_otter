from django.urls import URLPattern, path
from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name = "index"),
    path('create', views.create, name = "create"),
    path('<int:pk>/mark_complete', views.mark_complete, name = "mark_complete"),    
    path('<int:pk>/delete', views.delete, name = "delete"),
]