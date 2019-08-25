from django.db import models

from django.contrib.auth.models import User,Group
from user_profile.models import *

# Create your models here.

class SelectionModel(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)

