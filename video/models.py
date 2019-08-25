from django.db import models

from mooc_site.settings import MEDIA_ROOT
from user_profile.models import *

# Create your models here.
class VideoModel(models.Model):
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    name=models.TextField()
    source=models.FileField(upload_to=MEDIA_ROOT)