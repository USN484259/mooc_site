from django.db import models

from user_profile.models import *

# Create your models here.
class VideoModel(models.Model):
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    sorting=models.IntegerField()
    name=models.CharField(max_length=80)
    description=models.TextField(blank=True,null=True)
    source=models.FileField()
    class Meta:
        ordering = ['sorting']
