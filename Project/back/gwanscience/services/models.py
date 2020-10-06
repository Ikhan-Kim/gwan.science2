from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# Create your models here.

class NameCompat(models.Model):
    name1 = models.TextField()
    name2 = models.TextField()
    jumsu1 = models.IntegerField(default=0)
    jumsu2 = models.IntegerField(default=0)

class FaceReadingInfo(models.Model):
    eyebrow_shape = models.TextField()
    eyebrow_interval = models.TextField()
    eye_size = models.TextField()
    eye_interval = models.TextField()
    eye_tail = models.TextField()
    nose_length = models.TextField()
    nose_width = models.TextField()
    mouth_length = models.TextField()
    mouth_thickness = models.TextField()
    mouth_tail = models.TextField()
    eyebrow_result = models.TextField()
    eye_result = models.TextField()
    nose_result = models.TextField()
    mouth_result = models.TextField()
    total = models.TextField()
    total_result = models.TextField()
    user_img = models.ImageField(blank=True, upload_to="facePhotos")

class FaceImage(models.Model):
    user_img = models.ImageField(blank=True, upload_to="facePhotos")
    user_img2 = ProcessedImageField(upload_to='facePhotos',
                                            processors=[ResizeToFit(upscale=False)],
                                            format='JPEG',
                                            options= {'quality': 90 },
                                            )
