from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from posts.models import Posts, Commentaries, Post_Like
from user.models import Users, Follow
import datetime

# Create your views here.

def post(request):
    message = request.GET["message"]

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("main:index"))
    
    current_time = datetime.datetime.now()

    Posts.objects.create(
        text = message, 
        posting_time = current_time,
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

    try:
        referer = request.META.get('HTTP_REFERER')
    except:
        referer = reverse("main:index")



    return HttpResponseRedirect(referer)

    
def follow(request):
    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("user:login"))

    follower = request.user
    target_username = request.GET["username"]
    target = Users.objects.get(username = target_username)


    try:
        redirect = request.META.get('HTTP_REFERER')
    except:
        redirect = reverse("main:index")

    Follow.objects.create(
        follower = follower,
        target = target
    )


    return HttpResponseRedirect(redirect)


def unfollow(request):

    
    
    try:
        username = request.GET["username"]
    except:
        #ERROR
        return HttpResponseRedirect(reverse("main:index"))
    
    target_user = Users.objects.get(username = username)
    print(target_user)
    Follow.objects.filter(follower = request.user, target = target_user).delete()

    try:
        redirect = request.META.get('HTTP_REFERER')
    except:
        redirect = reverse("main:index")

    return HttpResponseRedirect(redirect)
    

def post_like(request):

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("user:login"))
    
    try:
        id = request.GET["id"]
    except:
        #ERROR
        return HttpResponseRedirect(reverse("main:index"))
    

    if len(Post_Like.objects.filter(user = request.user, post = id)) > 0:
        #Already liked
        return HttpResponseRedirect(reverse("main:index"))

    post = Posts.objects.get(pk = id)
    Post_Like.objects.create(user = request.user, post = post)


    try:
        redirect = request.META.get('HTTP_REFERER')
    except:
        redirect = reverse("main:index")

    return HttpResponseRedirect(redirect)