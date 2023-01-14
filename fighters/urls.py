from django.urls import path

from .views import FighterListView, FighterDetailView

urlpatterns = [
    path('', FighterListView.as_view(), name='fighter_main'),
    path('<slug:fighter_slug>/', FighterDetailView.as_view(), name='fighter_post'),

]
