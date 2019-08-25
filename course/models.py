from django.db import models

from django.contrib.auth.models import User,Group

# Create your models here.
class CourseModel(models.Model):
    name=models.TextField()
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)
