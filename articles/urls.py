from django.conf.urls import url, include
from rest_framework import routers
from .resources import ArticleViewSet, CategoryViewSet, ReactionViewSet
from.views import ArticleList

router = routers.DefaultRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'reactions', ReactionViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('article_list/', ArticleList.as_view()),
]