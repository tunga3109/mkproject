from django.contrib import admin
from django.urls import path
from .views import MainTemplateView, BlogListView, ContactTemplateView, PostDetailView, RegisterCreateView, SignInView, SearchResultsView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='blog_main'),
    path('contact/', ContactTemplateView.as_view(), name='blog_contact'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='blog_post'),
    path('signup/', RegisterCreateView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("search/", SearchResultsView.as_view(), name="search_results")
]