from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView

from blog.forms import ContactForm, LoginForm
from blog.models import Category, Contact, Post


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
    }


class MainTemplateView(TemplateView, BaseMixin):
    template_name = 'blog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'MORTAL KOMBAT FANPAGE'
        context['subheading'] = 'CHOOSE YOUR DESTINY'
        context['email'] = 'tunga3109@gmail.com'
        context.update(self.context)
        return context


class PostDetailView(BaseMixin, DetailView):
    template_name = 'blog/single-blog.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        return context


class BlogListView(ListView, BaseMixin):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'BLOG'
        context['email'] = 'tunga3109@gmail.com'
        context['categories'] = Category.objects.all()
        context.update(self.context)
        return context


class ContactTemplateView(BaseMixin, TemplateView):
    template_name = 'blog/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('blog_contact')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['form'] = ContactForm()
        context['heading'] = 'Contact'
        context['email'] = 'tunga3109@gmail.com'
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('form_type') == 'contact_form':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

        return self.get(request=request)


class SignInView(LoginView, BaseMixin):
    form_class = LoginForm
    template_name = 'blog/signin.html'
    success_url = reverse_lazy('blog_main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['heading'] = 'Sign In'
        context['email'] = 'tunga3109@gmail.com'
        return context
