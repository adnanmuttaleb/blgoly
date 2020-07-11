from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Article, Category, Reaction
from .serializers import ArticleSerializer, CategorySerializer, ReactionSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReactionViewSet(viewsets.ViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

    def create(self, request):
        user = request.user
        article = Article.objects.get(id=request.data["article_id"])
        type = request.data["type"]

        reaction = Reaction.objects.create(
            user=user,
            article=article,
            type=type
        )

        return Response(status=status.HTTP_201_CREATED)
