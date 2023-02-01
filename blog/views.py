from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView

from blog.forms import ContactForm, CommentForm
from blog.models import Category, Contact, Post, Comment, Profile
from fighters.models import Fighter
from django.db.models import Q


class BaseMixin:
    context = {
        'twitter': 'https://twitter.com',
        'facebook': 'https://facebook.com',
    }


class MainTemplateView(BaseMixin, TemplateView):
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
        context['recent_posts'] = Post.objects.order_by('-date_created')[:3]

        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-created_on')
        context['comments'] = comments_connected
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user)
        new_comment = Comment(body=request.POST.get('body'), user=profile[0], post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class BlogListView(BaseMixin, ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'BLOG'
        context['email'] = 'tunga3109@gmail.com'
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.order_by('-date_created')[:3]
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


class SearchResultsView(BaseMixin, ListView):
    model = Post
    template_name = "blog/search_results.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.order_by('-date_created')[:3]
        return context

    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(descr__icontains=query)
        )
        return object_list


class CategoryListView(BaseMixin, ListView):
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'
    paginate_by = 3
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'Categories'
        context.update(self.context)
        return context


# class BlogFilterCategoryListView(BaseMixin, ListView):
#     template_name = 'blog/posts_filter_category.html'
#     paginate_by = 3
#     context_object_name = 'posts'
#     model = Post
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         context['categories'] = Category.objects.all()
#         context['recent_posts'] = Post.objects.order_by('-date_created')[:3]
#         context.update(self.context)
#         return context


def post_category(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-date_created')[:3]

    return render(request, 'blog/posts_filter_category.html', {'posts': posts, 'categories': categories, 'recent_posts': recent_posts})
