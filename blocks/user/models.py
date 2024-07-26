from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser



# class Users(AbstractBaseUser):
#     username = models.CharField(max_length=50, unique=True)
#     first_name = models.CharField(max_length=50, default="")
#     last_name = models.CharField(max_length=50, default="")
#     email = models.EmailField(unique=True, max_length=75, blank=False, null=False, default="")
#     image = models.ImageField(upload_to="user/avatars", null=False, blank=False, verbose_name="Аватар", default="/static/img/avatar-fat.jpg")
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"

#     def __str__(self):
#         return self.username
    
#     USERNAME_FIELD = "username"

class Users(AbstractUser):
    image = models.ImageField(upload_to="user/avatars", null=True, blank=True, verbose_name="Аватар", default="/static/img/avatar-fat.jpg")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username