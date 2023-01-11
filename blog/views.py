from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blog.models import Post


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
        context['phone'] = '+375336377999'
        context['email'] = 'tunga3109@gmail.com'
        context.update(self.context)
        return context


class BlogListView(ListView, BaseMixin):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'BLOG'
        context.update(self.context)
        return context
