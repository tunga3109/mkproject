from django.contrib import admin
from django.urls import path
from .views import MainTemplateView, BlogListView


urlpatterns = [
    path('', MainTemplateView.as_view(), name='blog_main'),
    path('blog/', BlogListView.as_view(), name='blog_list'),

]