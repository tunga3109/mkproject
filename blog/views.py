from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView

from blog.forms import ContactForm, LoginForm, RegisterForm, CommentForm
from blog.models import Category, Contact, Post, Comment
from fighters.models import Fighter
from django.db.models import Q


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
        context['posts'] = Post.objects.all()
        context['fighters'] = Fighter.objects.all()[:3]
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
        context['comment_form'] = CommentForm()
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()

        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-created_on')
        context['comments'] = comments_connected[:4]
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'), name=self.request.user, post=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


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


class RegisterCreateView(CreateView):
    form_class = RegisterForm
    template_name = 'blog/signup.html'
    success_url = reverse_lazy('signin')


class SearchResultsView(ListView, BaseMixin):
    model = Post
    template_name = "blog/search_results.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()[:2]
        return context

    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(descr__icontains=query)
        )

        return object_list
