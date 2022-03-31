# from django.urls import path
# from rest_framework.routers import DefaultRouter

# from . import views

# router = DefaultRouter()
# router.register('pokemon', views.PokemonViewSet, basename='pokemon')
# router.register('users', views.UserViewSet, basename='users')
# # router.register('users', views.CurrentUserView, basename='users')

# urlpatterns = router.urls 
# + [
#     path('currentuser/', views.CurrentUserView.as_view())
# ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.PokemonList.as_view()),
    path('<int:pk>/', views.PokemonDetail.as_view()),
    path('type/', views.TypeList.as_view()),
    path('type/<int:pk>/', views.TypeDetail.as_view()),
    
]