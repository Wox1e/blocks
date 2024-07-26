from django.contrib import admin
from user.models import Users


@admin.register(Users)
class user_admin(admin.ModelAdmin):
    pass