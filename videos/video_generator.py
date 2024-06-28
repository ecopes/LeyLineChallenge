import threading
import time
from threading import Thread

from images.daos import ImageDao
from utils import redis_queue as queue

lock = threading.Lock()


def video_start_creating(image_id):
    queue.enqueue(queue.IMAGE_QUEUE_NAME, str(image_id))


def generate_video():
    Thread(target=_generate_video).start()


def _generate_video():
    print("video-generator: Start generating video...")
    while True:
        image_id = queue.dequeue(queue.IMAGE_QUEUE_NAME)
        if not image_id:
            print("video-generator: Queue is empty, sleeping 10 seconds")
            time.sleep(10)
            continue
        image_id = image_id.decode('utf-8')
        # here I'm going to sleep 30 seconds, but also update the percentage of the creation
        for i in range(1, 16):
            percentage_video_created = int(i / 15 * 100)
            ImageDao.set_percentage_video_created(image_id, percentage_video_created)
            time.sleep(2)
