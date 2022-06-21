from dataclasses import field
from rest_framework import serializers

from user.serializers import UserSerializer
from blog.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
  # OnetoOneField 이므로 user 명칭으로 역참조 가능
  # user = UserSerializer()
  category = CategorySerializer(many=True)
  
  class Meta:
    model = Article
    fields = ['user', 'title', 'category', 'content']