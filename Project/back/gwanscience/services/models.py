from django.db import models

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
    mouse_length = models.TextField()
    mouse_thickness = models.TextField()
    mouse_tail = models.TextField()
    eyebrow_result = models.TextField()
    eye_result = models.TextField()
    nose_result = models.TextField()
    mouse_result = models.TextField()
    total_result = models.TextField()