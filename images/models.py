from django.db import models

from utils.common_models import BaseModel


def get_default_file():
    return 'saved_videos/default.mp4'


class Image(BaseModel):
    image = models.ImageField(upload_to='saved_images/')
    percentage_video_created = models.IntegerField(default=0)
    video = models.FileField(upload_to='saved_videos/')

    def save(self, *args, **kwargs):
        self.video = get_default_file()
        super().save(*args, **kwargs)
