from pika.adapters import blocking_connection
from amqp_utils.amqp_client import get_connection
import time


def produce_message(channel: blocking_connection.BlockingConnection) -> None:
    QUEUE = 'weather'
    channel.queue_declare(QUEUE)

    message = 'Weather from Oleksandr Chykota: sunny, message {item}'
    for item in range(2210):
        time.sleep(0.1)
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message.format(item=item)
        )
        print('Sent:', message.format(item=item))


def main_producer():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel)