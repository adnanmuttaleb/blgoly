from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Article, Category, Reaction
from .serializers import ArticleSerializer, CategorySerializer, ReactionSerializer, ReactionToArticleSerializer


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
        serializer = ReactionToArticleSerializer(user=request.user, data=request.data)
        if serializer.is_valid():
            reaction = Reaction(
                user=request.user,
                article=serializer.validated_data["article_id"],
                type=serializer.validated_data["type"]
            )
            reaction.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
