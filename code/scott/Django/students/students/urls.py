from django.urls import path
from django.views.generic import TemplateView


app_name = 'students'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]
# from . import views
# from .views import StudentListView

# # urlpatterns = [
# #     path('', StudentListView.as_view(), name='home')
# # ]