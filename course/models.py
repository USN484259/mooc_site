from django.db import models

from django.contrib.auth.models import User,Group

# Create your models here.
class CourseModel(models.Model):
    name=models.CharField(max_length=80)
    description=models.TextField()
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name+'_'+str(self.teacher)