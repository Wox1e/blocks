from django.contrib import admin
from user.models import Users, Follow


@admin.register(Users)
class user_admin(admin.ModelAdmin):
    pass

@admin.register(Follow)
class follow_admin(admin.ModelAdmin):
    pass