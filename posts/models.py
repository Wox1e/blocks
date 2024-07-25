#from user.models import Users, default_User
from django.db import models
from user.models import Users
# Create your models here.
        


class Posts(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Текст поста")
    posting_time = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = ("Пост")
        verbose_name_plural = ("Посты")




class Commentaries(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Текст комментария")
    post = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Комментарий")
        verbose_name_plural = ("Комментарии")


