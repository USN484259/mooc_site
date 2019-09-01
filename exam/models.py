from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User,Group
from course.models import *
from user_profile.models import *

# Create your models here.
class ExamModel(models.Model):
    name=models.CharField(max_length=80)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE)
    sorting=models.IntegerField()
    question=RichTextUploadingField()
    score=models.FloatField()
    class Meta:
        ordering = ['sorting']


class ScoreModel(models.Model):
    selection=models.ForeignKey(SelectionModel,on_delete=models.CASCADE)
    exam=models.ForeignKey(ExamModel,on_delete=models.DO_NOTHING)
    answer=RichTextUploadingField()
    total=models.FloatField()
    score=models.FloatField(null=True)