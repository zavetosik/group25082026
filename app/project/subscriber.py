from redis_utils.redis_client import redis_client

subscriber = redis_client.pubsub()
subscriber.subscribe("python_channel")

for message in subscriber.listen():
    if message["type"] == "message":
        print(message["data"])