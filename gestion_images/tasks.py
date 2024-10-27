# gestion_images/tasks.py
from celery import shared_task
from PIL import Image as PilImage
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Image

@shared_task
def generate_thumbnail(image_id):
    image = Image.objects.get(id=image_id)
    img = PilImage.open(image.image)
    img.thumbnail((100, 100))
    thumb_io = BytesIO()
    img.save(thumb_io, img.format)
    image.thumbnail.save(image.image.name, ContentFile(thumb_io.getvalue()), save=False)
    image.save()
