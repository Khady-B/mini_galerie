from django.shortcuts import render

# Create your views here.

# gestion_images/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from .tasks import generate_thumbnail

class ImageUploadView(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()
            generate_thumbnail.delay(image.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageListView(APIView):
    def get(self, request):
        images = Image.objects.all().order_by('-uploaded_at')
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class ImageListCreate(APIView):
    queryset = Image.objects.all().order_by('-upload_date')
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image = serializer.save()
        generate_thumbnail.delay(image.id)

class ImageListDelete(APIView):
    queryset = Image.objects.all().order_by('-upload_date')
    serializer_class = ImageSerializer

    def perform_remove(self, serializer):
        image = serializer.remove()
        return Response(serializer.data)