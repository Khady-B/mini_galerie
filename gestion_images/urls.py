# gestion_images/urls.py
from django.urls import path
from .views import ImageUploadView, ImageListView, ImageListCreate, ImageListDelete

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('images/', ImageListView.as_view(), name='image-list'),
    path('add/', ImageListCreate.as_view(), name='image-list-create'),
    path('remove/', ImageListDelete.as_view(), name='image-list-delete'),
]
