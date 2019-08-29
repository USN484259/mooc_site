from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from course.models import *
# class BlogType(models.Model):
	# type_name = models.CharField(max_length = 15)

	# def __str__(self):
		# return self.type_name

class Blog(models.Model):
	title = models.CharField(max_length = 50)
	reference = models.ForeignKey(CourseModel, on_delete = models.CASCADE)
	content = RichTextUploadingField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	created_time = models.DateTimeField(auto_now_add = True)
	last_updated_time = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "<Blog: %s>" % self.title

	class Meta:
		ordering = ['-created_time']



