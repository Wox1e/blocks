from django.http import JsonResponse
from posts.models import Posts
from main.templatetags.get_time_difference import get_time_difference
from main.templatetags.get_commentaries import get_commentaries
# Create your views here.


def load_more(request):
    offset = int(request.GET.get('offset'))
    limit = int(request.GET.get('limit'))
    posts = Posts.objects.all().order_by("-posting_time")[offset: offset + limit]
    
    response = []
    for post in posts:

        data = {
            "id":post.id,
            "posting_time":get_time_difference(post.posting_time),
            "username":post.user.username,
            "likes":post.likes,
            "text":post.text,
            "is_liked":bool(post.is_liked(request.user)),
            "image":str(post.user.image),
        }

        response.append(data)

    
    return JsonResponse(response, safe=False)