import redis
import config
import datetime

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)


redis_client.set("favorite_car", "porsche")

redis_client.set("Pet", "Sandy", ex=7200)

redis_client.rpush("shopping_list", "milk", "eggs", "bread")
redis_client.expireat("shopping_list", datetime.datetime.now() + datetime.timedelta(days=7))

redis_client.hset("cake", mapping={
    "flour": 250,
    "milk": 500,
})

redis_client.hset("cake", "sugar", 300)

redis_client.hset("cake", "sugar", 500)