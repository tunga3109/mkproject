from django.urls import path
from .views import MainTemplateView, BlogListView, ContactTemplateView, PostDetailView, SearchResultsView, CategoryListView, post_category

urlpatterns = [
    path('', MainTemplateView.as_view(), name='blog_main'),
    path('contact/', ContactTemplateView.as_view(), name='blog_contact'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path("blog/category/", CategoryListView.as_view(), name="category_list"),
    path("blog/category/<slug:slug>", post_category, name="category_list_filter"),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='blog_post'),
    path("search/", SearchResultsView.as_view(), name="search_results"),

]