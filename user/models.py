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
    
class Follow(models.Model):
    follower = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Подписчик", related_name='follower') #related_name='follows' ! can be bugs
    target = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name="Цель подписки", related_name='target') #related_name='follows' ! can be bugs

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
    
    def __str__(self):
        return f"Подписка {self.follower} на {self.target}"