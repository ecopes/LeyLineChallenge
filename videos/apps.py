from django.apps import AppConfig


class VideoConfig(AppConfig):
    name = 'videos'

    def ready(self):
        import os
        if os.environ.get('RUN_MAIN'):
            from threading import Thread
            from videos import video_generator
            Thread(target=video_generator.generate_video, args=()).start()
