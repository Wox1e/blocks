from django import template

register = template.Library()

@register.inclusion_tag('main/infinite_scroll.html')
def infinite_scroll():
    return {}