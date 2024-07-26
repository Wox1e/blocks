from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from user.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from blocks.settings import DEBUG
from user.models import Users
from posts.models import Posts, Commentaries


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
            print(user)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("user:profile", kwargs={"username":request.user.username}))
            

    else:
        form = UserRegisterForm()



    context = {
        "form":form

    }

    return render(request, "user/register.html", context)





def profile(request, username):

    try:
        user = Users.objects.get(username = username)
    except Users.DoesNotExist:
        user = None


    if user == None:
        #Пользователь не найден
        #redirect
        return HttpResponseRedirect(reverse("main:index"))
    
    
    posts = Posts.objects.all().filter(user = user)
    has_posts = len(posts) > 0



    context = {
        "user":user,
        "posts":posts,
        "has_posts":has_posts,

    }

    return render(request, "user/profile.html", context)


def logout(request):
    print(request)
    auth.logout(request)

    return HttpResponseRedirect(reverse("user:login"))