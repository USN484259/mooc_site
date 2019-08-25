from django.urls import path,include

from .views import *

urlpatterns=[
    path("<int:id>",show_course,name="course"),

]