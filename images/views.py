import os

from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from images import models
from images import serializers
from videos import video_generator


class UploadImageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()
            video_generator.video_start_creating(image_id=image.id)
            return Response({"info": "image saved", "id": image.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoPercentageView(APIView):

    def get_object(self, pk):
        try:
            return models.Image.objects.get(pk=pk)
        except models.Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        return Response({"percentage": image.percentage_video_created if image else 0}, status=status.HTTP_200_OK)


class VideoView(APIView):

    def get_object(self, pk):
        try:
            return models.Image.objects.get(pk=pk)
        except models.Image.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        video_path = os.path.join(str(image.video))
        if os.path.exists(video_path):
            with open(video_path, 'rb') as playlist_file:
                playlist_data = playlist_file.read()

            response = HttpResponse(playlist_data, content_type='application/vnd.apple.mpegurl')
            return response
        else:
            return HttpResponse('Video file not found.', status=404)
