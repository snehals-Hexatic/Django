from celery import shared_task
from time import sleep


@shared_task(bind=True)
def sub(self, x, y):
    """
    Simple background task example
    """
    sleep(10)
    return x - y


@shared_task(bind=True)
def clear_session_cache(self, session_id):
    """
    Clear Django session cache (example)
    """
    print(f"Session Cache Cleared: {session_id}")
    return session_id


@shared_task(bind=True)
def clear_redis_data(self, key):
    """
    Clear Redis data (example)
    """
    print(f"Redis Data Cleared: {key}")
    return key


@shared_task(bind=True)
def clear_rabbitmq_data(self, key):
    """
    Clear RabbitMQ data (example)
    """
    print(f"RabbitMQ Data Cleared: {key}")
    return key
