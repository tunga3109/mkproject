from django.urls import path
from .views import RegisterCreateView, SignInView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', RegisterCreateView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]