from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class ArticleList(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
