#from user.models import Users, default_User

from django.db import models
from user.models import Users
import redis
import config
# Create your models here.

redis_db = redis.Redis(
    host=config.REDIS_HOST, 
    port = config.REDIS_PORT
    )


class Posts(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Текст поста")
    posting_time = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    def get_int_likes(self):
        return len(Post_Like.objects.filter(post = self))

    @property
    def likes(self):

        pk = f"post:{self.id}_likes"    
        num_likes = redis_db.get(pk)
        print(num_likes)

        if num_likes == None:
            num_likes = len(Post_Like.objects.filter(post = self))
            redis_db.set(name=pk, value=num_likes, ex=10)
        else:
            num_likes = int(num_likes)

        if num_likes > 1_000_000:
            return str(round(num_likes / 1_000_000, 1)) + "M"
        elif 1_000 <= num_likes < 1_000_000:
            return str(round(num_likes / 1000, 1)) + "k"
        else:
            return len(Post_Like.objects.filter(post = self))
        
    def is_liked(self, user):
        try:
            like_list = Post_Like.objects.filter(post = self, user = user)
            return len(like_list) > 0
        except:
            return False

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


class Post_Like(models.Model):
    user = models.ForeignKey(to=Users,on_delete=models.CASCADE)
    post = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Лайк")
        verbose_name_plural = ("Лайки")

    def __str__(self):
        return f"{self.user} liked {self.post}"
