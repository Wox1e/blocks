
import pika
import jwt




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