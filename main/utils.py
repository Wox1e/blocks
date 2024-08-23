import requests
from posts.models import Posts, Users
from django.core import serializers
from django.db.models import QuerySet
import pika
import jwt




def check_cache_api():
    #bad working
    return requests.get("http://127.0.0.1:5000/check")

def get_post_from_cache(pk:int):
    pk = f"post{pk}"
    response = requests.get("http://127.0.0.1:5000/get", params = {"pk":pk})


    data = response.json()
    for deserialized_object in serializers.deserialize("json", data):
        return deserialized_object.object

    # def get_posts_from_cache(pk_list:list[int]):
    #     for pk in pk_list:
    #         print(get_post_from_cache(pk))



def send_post_to_cache(post:Posts, time:int):
    pk = f"{post.user.username}_post{post.pk}"
    post_list = [post,]
    data = serializers.serialize("json", post_list)
    requests.post("http://127.0.0.1:5000/send", params = {"pk":pk, "time":time}, json=data)


def send_posts_to_cache(queryset:QuerySet, time:int):
    for object in queryset:
        send_post_to_cache(object, time=time)

def send_profile_to_cache(user:Users, time:int):
    pk = f"profile_{user.username}"
    data = serializers.serialize("json", [user,])
    requests.post("http://127.0.0.1:5000/send", params = {"pk":pk, "time":time}, json=data)

def get_profile_from_cache(username:str):
    pk = f"profile_{username}"
    response = requests.get("http://127.0.0.1:5000/get", params = {"pk":pk})
    data = response.json()

    if not data:
        return False
        
    for deserialized_object in serializers.deserialize("json", data):
        return deserialized_object.object
        
        
def send_user_posts_to_cache(username:str, time:int):
    user = Users.objects.get(username = username)
    for post in Posts.objects.filter(user=user):
        pk = f"{username}_post_{post.pk}"
        send_post_to_cache(post, time = time) 

def get_user_posts_from_cache(username:str):
    pk = f"{username}_post"
    response = requests.get("http://127.0.0.1:5000/get/search", params={"starts_with":pk})
    
    data = response.json()



    if not data:
        return False
        
    for deserialized_object in serializers.deserialize("json", data):
        print(deserialized_object.object)


    #доделать



def publish_to_brocker(host:str, exchange:str, body:str, routing_key:str = "") -> None:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    channel.basic_publish(exchange=exchange,
                      routing_key=routing_key,
                      body=body)


def generate_jwt_token(user):
    SECRET_KEY = "(t6qy$9%y=1tqo!8ps((!%w0u#lve_onrl4z-50z_gs6e!-t"
    payload = {
        'username': user.username,
        'password_hash': user.password,
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token