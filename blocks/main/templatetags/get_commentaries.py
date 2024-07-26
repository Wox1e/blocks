from django import template
from posts.models import Posts, Commentaries 

register = template.Library()

@register.simple_tag
def get_commentaries(post:Posts):
    commentaries = Commentaries.objects.filter(post=post)
    #print("comms=",commentaries)
    return commentaries