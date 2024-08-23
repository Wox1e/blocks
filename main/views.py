from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from posts.models import Posts
import datetime



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