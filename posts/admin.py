from django.contrib import admin
from posts.models import Posts, Commentaries
# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Commentaries)
class CommentariesAdmin(admin.ModelAdmin):
    pass