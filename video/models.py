from django.db import models

# Create your models here.
class VideoModel(models.Model):
    name=models.TextField()
    source=models.TextField()