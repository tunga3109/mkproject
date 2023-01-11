from django.contrib import admin
from django.urls import path
from .views import MainTemplateView, BlogListView, ContactTemplateView


urlpatterns = [
    path('', MainTemplateView.as_view(), name='blog_main'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('contact/', ContactTemplateView.as_view(), name='blog_contact'),


]