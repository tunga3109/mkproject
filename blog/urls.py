from django.urls import path
from .views import MainTemplateView, BlogListView, ContactTemplateView, PostDetailView, SearchResultsView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='blog_main'),
    path('contact/', ContactTemplateView.as_view(), name='blog_contact'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='blog_post'),
    path("search/", SearchResultsView.as_view(), name="search_results")
]