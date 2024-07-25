from django.shortcuts import render
from posts.models import Posts
import datetime

# Create your views here.


def index(request):
    user = request.user

    posts = Posts.objects.all().order_by('-posting_time')
    has_posts = len(posts) > 0
    current_time = datetime.datetime.now()


    context = {
        "title":"Лента",
        "posts":posts,
        "has_posts":has_posts,
        "user":user
        

    }

    return render(request,"main/index.html", context)