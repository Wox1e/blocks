from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from blocks.settings import DEBUG
from user.models import Users, Follow
from posts.models import Posts, Commentaries
from main.utils import *
import json



# Create your views here.


def login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:profile", kwargs={"username":request.user.username}))


    #DEBUG LOGIC
    if DEBUG:
        print("method =", request.method)
        if request.method == "POST":
            print("username =", request.POST["username"])
            print("password =", request.POST["password"])
        else:
            print(request.GET)
    #DEBUG LOGIC


    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))


    else:
        form = UserLoginForm()





    
    context = {
        "form":form
    }

    return render(request, "user/login.html", context)

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():

        


            form.save()
            
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password1"])
            if user:

                #to rabit mq

                data = {
                    "username":request.POST["username"],
                    "password":user.password,
                    "email":request.POST["email"],
                    "first_name":request.POST["first_name"],
                    "last_name":request.POST["last_name"]
                }

                body = json.dumps(data)

                publish_to_brocker("localhost", "blocks-ex-direct-all", body)

                #

                auth.login(request, user)
                return HttpResponseRedirect(reverse("user:profile", kwargs={"username":request.user.username}))
            

    else:
        form = UserRegisterForm()



    context = {
        "form":form

    }

    return render(request, "user/register.html", context)


def change_avatar(request):

    if not request.user.is_authenticated:
        #NOT AUTH LOGIC
        return HttpResponseRedirect(reverse("user:login"))

    user = request.user


    try:
        redirect = request.META.get('HTTP_REFERER')
    except:
        redirect = reverse("main:index")

    return HttpResponseRedirect(redirect)




def profile(request, username):

    #caching
    # if check_cache_api:
    #     user = get_profile_from_cache(username)

    #     if not user:
    #         try:
    #             user = Users.objects.get(username = username)
    #             send_profile_to_cache(user, time=50)
    #         except Users.DoesNotExist:
    #             user = None
    # else:
    #     user = user = Users.objects.get(username = username)
    
    ###

    
    ##caching posts

    # get_user_posts_from_cache(user.username)

    ###

    #remove when caching
    user = user = Users.objects.get(username = username)

    if user == None:
        #Пользователь не найден
        #redirect
        return HttpResponseRedirect(reverse("main:index"))
    
    
    posts = Posts.objects.all().filter(user = user).order_by("-posting_time")
    has_posts = len(posts) > 0
    posts_num = len(posts)

    follows = Follow.objects.all().filter(follower = user)
    follows_num = len(follows)

    followers = Follow.objects.all().filter(target = user)
    followers_num = len(followers)

    if request.user.is_authenticated:
        is_followed = len(Follow.objects.filter(follower = request.user, target = user)) > 0
    else:
        is_followed = False


    view_as = "" #owner, follower, default
    #to do!!!!!

    is_owner = user == request.user


    context = {
        "user":user,
        "posts":posts,
        "has_posts":has_posts,
        "posts_num":posts_num,
        "follows_num":follows_num,
        "followers_num":followers_num,
        "is_followed":is_followed,
        "is_owner":is_owner
    }

    return render(request, "user/profile.html", context)


def logout(request):
    print(request)
    auth.logout(request)

    return HttpResponseRedirect(reverse("user:login"))