from rest_framework import serializers
from .models import Categories, Articles

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'url', 'name')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'url', 'link', 'rating', 'categories')
