from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from blog.models import Category, Post
from fighters.models import Fighter


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'descr', 'image', 'category')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class FighterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Fighter
        fields = ('id', 'character_name', 'descr', 'image')
