from django.db import models

# Create your models here.

class NameCompat(models.Model):
    name1 = models.TextField()
    name2 = models.TextField()
    jumsu1 = models.IntegerField(default=0)
    jumsu2 = models.IntegerField(default=0)