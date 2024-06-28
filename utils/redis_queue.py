import redis

redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
IMAGE_QUEUE_NAME = "image_queue"


def enqueue(queue_name, item):
    try:
        redis_client.rpush(queue_name, item)
    except Exception as e:
        print(f"Error enqueueing item: {e}")


def dequeue(queue_name):
    try:
        return redis_client.lpop(queue_name)
    except Exception as e:
        print(f"Error dequeuing item: {e}")
        return None
