

from django import template

register = template.Library()

@register.filter
def to_spacce(value):
    return value.replace("_"," ")