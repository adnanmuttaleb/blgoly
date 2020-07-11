from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Article, Reaction, Category


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'description', 'publish_date', 'likes', 'author']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['user', 'article', 'type']


class ReactionToArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField()
    type = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def validate_article_id(self, art_id):
        try:
            return Article.objects.get(id=art_id)
        except:
            ValidationError("Article Does not Exist")