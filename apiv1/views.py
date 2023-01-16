from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from blog.models import Category, Post
from fighters.models import Fighter

from .serializers import PostSerializer, CategorySerializer, FighterSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_published=True)
    serializer_class = CategorySerializer


# class FightersViewSet(ModelViewSet):
#     queryset = Fighter.objects.all()
#     serializer_class = FighterSerializer


class FighterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['character_name']
