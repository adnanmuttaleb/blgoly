from django.contrib import admin
from .models import Article, Category, Reaction


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'author')
    list_display = ('title', 'publish_date', 'likes')
    date_hierarchy = 'publish_date'


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    pass
