from django.db import models

from user_profile.models import *

# Create your models here.
class VideoModel(models.Model):
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    name=models.TextField()
    source=models.FileField()