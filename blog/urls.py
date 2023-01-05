from django.contrib import admin
from django.urls import path
from .views import MainTemplateView


urlpatterns = [
    path('main/', MainTemplateView.as_view(), name='blog_main'),
]