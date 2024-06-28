from django.urls import re_path
from rest_framework import routers

from images import views as image_views

router = routers.DefaultRouter()

urlpatterns = [
    re_path(
        "upload_image/",
        image_views.UploadImageView.as_view(),
        name='upload-image',
    ),
    re_path(
        r'^video/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})/percentage/$',
        image_views.VideoPercentageView.as_view(),
        name='video-percentage',
    ),
    re_path(
        r'^video/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})/view/$',
        image_views.VideoView.as_view(),
        name='video-percentage',
    ),
]

urlpatterns += router.urls
