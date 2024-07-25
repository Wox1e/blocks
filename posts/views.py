from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from posts.models import Posts, Commentaries
from user.models import Users
import datetime

# Create your views here.

def post(request):
    message = request.GET["message"]

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("main:index"))

    Posts.objects.create(
        text = message, 
        posting_time = datetime.datetime.now(),
        user = request.user
    )

    return HttpResponseRedirect(reverse("main:index"))    

def commentary(request):

    

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("main:index"))
    
    post_id = request.GET["post_id"]
    user_id = request.user.id
    text = request.GET["message"]

    post = Posts.objects.get(id = post_id)
    user = Users.objects.get(id = user_id)

    Commentaries.objects.create(
        text = text,
        post = post,
        user = user
    )

    
    return HttpResponseRedirect(reverse("main:index"))

    