import json
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from posts.models import Posts
import datetime
from main.templatetags.get_time_difference import get_time_difference
from main.templatetags.get_commentaries import get_commentaries



# Create your views here.

#caching
from main.utils import *


#

def index(request):
    user = request.user
    
   

    

    # ##go to cache
    # try:
    #     check_cache_api()
    # except:
    #     print("api not work")
    # ##
    

    posts = Posts.objects.all().order_by('-posting_time')[:10]

    
    


    has_posts = len(posts) > 0
    current_time = datetime.datetime.now()


    context = {
        "title":"Лента",
        "posts":posts,
        "has_posts":has_posts,
        "user":user
    }


    return render(request,"main/index.html", context)



def messages(request):
    
    messages_url = "http://127.0.0.1:8080/"

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("user:login"))
    
    try:
        response = requests.request(url=messages_url, method="GET")
    except:
        #not working logic
        return HttpResponseRedirect(reverse("main:index"))

    token = generate_jwt_token(request.user)
    url = f'http://localhost:8080/auth?token={token}'

    return redirect(url)




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