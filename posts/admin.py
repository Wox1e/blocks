from django.contrib import admin
from posts.models import Posts, Commentaries, Post_Like
# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Commentaries)
class CommentariesAdmin(admin.ModelAdmin):
    pass

@admin.register(Post_Like)
class Post_LikeAdmin(admin.ModelAdmin):
    pass