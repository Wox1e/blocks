"""
URL configuration for blocks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from posts import views

app_name = "posts"

urlpatterns = [
    path("post/", views.post, name = "post"),
    path("commentary/", views.commentary, name = "commentary"),
    path("follow/", views.follow, name = "follow"),
    path("unfollow/", views.unfollow, name="unfollow"),
    path("post_like/", views.post_like, name="post_like"),
    path("post_unlike/", views.post_unlike, name = "post_unlike"),
]
