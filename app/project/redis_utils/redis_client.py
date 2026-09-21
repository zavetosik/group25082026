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


success = redis_client.set('foo', 'bar333333333333333')
# print(success)
redis_client.set('myKeyTTL', "SecretKey", ex=10)
redis_client.set('promo:1', "promocode", exat=datetime.datetime(year=2027, month=3, day=8))