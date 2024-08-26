from django.db import models
from django.contrib.auth.models import AbstractUser



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