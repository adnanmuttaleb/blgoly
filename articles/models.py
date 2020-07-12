from django.db import models
from django.conf import settings


class ReactionType(models.IntegerChoices):
    LIKE = 1


class Reaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    type = models.IntegerField(choices=ReactionType.choices)

    @staticmethod
    def reacted(user, article, type=ReactionType.LIKE):
        return Reaction.objects.filter(
            user=user,
            article=article,
            type=type
        ).exists()

    class Meta:
        unique_together = ('article', 'user', 'type')


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    reactors = models.ManyToManyField(settings.AUTH_USER_MODEL, through=Reaction, related_name='reactions')

    @property
    def likes(self):
        return self.reactors.filter(reaction__type=ReactionType.LIKE).count()

    def __str__(self):
        return self.title

