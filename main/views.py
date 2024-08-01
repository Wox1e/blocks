from django.shortcuts import render
from posts.models import Posts
import datetime
from django.core.paginator import Paginator

# Create your views here.

#caching
from main.utils import *


#

def index(request):
    user = request.user
    
    try:
        page = int(request.GET["page"])
    except:
        page = 1

    


    # ##go to cache
    # try:
    #     check_cache_api()
    # except:
    #     print("api not work")
    # ##
    

    posts = Posts.objects.all().order_by('-posting_time')
    
    #paginator = Paginator(posts,10)
    


    has_posts = len(posts) > 0
    current_time = datetime.datetime.now()


    context = {
        "title":"Лента",
        "posts":posts,
        "has_posts":has_posts,
        "user":user,
        #"page":page,
        #"paginator":paginator
    }


    return render(request,"main/index.html", context)