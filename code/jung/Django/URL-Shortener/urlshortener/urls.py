from django.urls import path
from . import views

app_name = 'urlshortener'

urlpatterns = [
    path('', views.index, name = "index"),
    path('<str:short_url>', views.redirect, name = "redirect"),
]





# from django.conf import settings
# import uuid
# u = uuid.uuid4()
# u.hex

# def create_shortened_url(model_instance):
#     model_class = model_instance.__class__
#     if model_class.objects.filter(short_url = u.hex).exists():
#         return create_shortened_url(model_instance)
#     return u.hex