from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.views import BaseMixin
from registration.forms import LoginForm, RegisterForm


class SignInView(BaseMixin, LoginView):
    form_class = LoginForm
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('blog_main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['form'] = LoginForm()
        context['heading'] = 'Sign In'
        return context


class RegisterCreateView(BaseMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('signin')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['form'] = RegisterForm()
        context['heading'] = 'Sign Up'
        return context


