from django.db import models
from django.db.models.base import ModelState
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # ['id', 'author', 'title']
