import requests
from posts.models import Posts
from django.core import serializers
from django.db.models import QuerySet


def check_cache_api():
    return requests.get("http://127.0.0.1:5000/check")

def get_post_from_cache(pk:int):
    pk = f"post{pk}"
    response = requests.get("http://127.0.0.1:5000/get_post", params = {"pk":pk})


    data = response.json()
    for deserialized_object in serializers.deserialize("json", data):
        return deserialized_object.object

# def get_posts_from_cache(pk_list:list[int]):
#     for pk in pk_list:
#         print(get_post_from_cache(pk))



def send_post_to_cache(post:Posts, time:int):
    pk = f"post{post.pk}"
    post_list = [post,]
    data = serializers.serialize("json", post_list)
    requests.post("http://127.0.0.1:5000/send_post", params = {"pk":pk, "time":time}, json=data)


def send_posts_to_cache(queryset:QuerySet, time:int):
    for object in queryset:
        send_post_to_cache(object, time=time)