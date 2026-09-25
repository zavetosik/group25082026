import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

AWS_REGION_NAME=os.getenv("AWS_REGION_NAME")
AWS_ENDPOINT_URL=os.getenv("AWS_ENDPOINT_URL")
AWS_ACCESS_KEY=os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY=os.getenv("AWS_SECRET_KEY")
AWS_PUBLIC_URL=os.getenv("AWS_PUBLIC_URL")
AWS_BUCKET_NAME=os.getenv("AWS_BUCKET_NAME")