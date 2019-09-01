from django.db import models

from django.contrib.auth.models import User,Group
from course.models import *

# Create your models here.

class SelectionModel(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)

    def __str(self):
        return self.student+"_"+self.course