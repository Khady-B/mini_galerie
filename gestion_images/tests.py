from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rest_framework.test import APIClient
from .models import Image

class ImageTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_image(self):
        with open('path/to/test/image.jpg', 'rb') as img:
            response = self.client.post('/api/images/', {'title': 'Test Image', 'image': img}, format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_list_images(self):
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)
