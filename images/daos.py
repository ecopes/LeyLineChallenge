from django.db import models

from images.models import Image


class ImageDao(models.Manager):
    @staticmethod
    def set_percentage_video_created(image_id, percentage_video_created):
        print(f"Updating image ({image_id}) percentage_video_created: {percentage_video_created}")
        Image.objects.filter(id=image_id).update(percentage_video_created=percentage_video_created)
