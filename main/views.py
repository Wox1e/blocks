from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from posts.models import Posts
import datetime
from main.utils import generate_jwt_token
from main.caching import *



def index(request):


    user = request.user
    posts = Posts.objects.all().order_by('-posting_time')[:10]
    has_posts = len(posts) > 0

    context = {
        "title":"Лента",
        "posts":posts,
        "has_posts":has_posts,
        "user":user,
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


