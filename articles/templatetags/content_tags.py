from django import template
from ..models import Reaction


register = template.Library()


@register.simple_tag
def reacted(user, article):
    return Reaction.reacted(user, article)