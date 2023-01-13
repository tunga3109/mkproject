from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from blog.forms import ContactForm
from blog.models import Contact, Post


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
        return context

    def post(self, request: HttpRequest):
        if request.POST.get('form_type') == 'contact_form':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

        return self.get(request=request)
