from redis_utils.redis_client import redis_client


for i in range(10):
    message = f"Hello Redis! Message #{i}"
    redis_client.publish("python_channel", message)
    print(message)