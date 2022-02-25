from django.urls import path
from . import views

app_name = 'short'
urlpatterns = [
    path('', views.index, name='index'),
    # I think the 'click_link_route_to_page' needs to be last since it was catching 'add/'. 'add/' needs to catch the route before it gets to 'click_link_route_to_page'. The '<str:code>' part is catching all strings?
    # TODO: Add a path before the '<str:code>' to make more robust.
    path('add/', views.add, name='add'),
    # NOTE: But I had to hard-code 'sc/' in between 'short:index' and 'shortcode_set.code', in index.html.
    path('sc/<str:code>/', views.click_link_route_to_page, name='click_link_route_to_page'),
]