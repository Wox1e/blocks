import os
from dotenv import load_dotenv

load_dotenv()

#REDIS_URI = os.getenv("REDIS_URI")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")