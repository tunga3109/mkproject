from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CategoryViewSet, FighterViewSet


api_router = SimpleRouter()
api_router.register(r'post', PostViewSet)
api_router.register(r'categories', CategoryViewSet)
api_router.register(r'fighter', FighterViewSet)

urlpatterns = [
    path('', include(api_router.urls)),
]
