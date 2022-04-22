from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import PokemonViewSet, TypeViewSet, CustomUserViewSet, CurrentUserView
from api.views import PokemonViewSet, TypeViewSet
# urlpatterns = [
#     # path('',  views.getRoutes),
#     path('pokemon/', views.PokemonViewSet.as_view(), name="pokemon"),
#     # path('users/', views.CustomUser_View.as_view()),
#     # path('types/', views.Type_View_Sets.as_view()),
# ]

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')
# router.register('users', CustomUserViewSet, basename='users')
urlpatterns = router.urls + [
    # path('currentuser/', CurrentUserView.as_view())
]