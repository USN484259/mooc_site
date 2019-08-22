from django.urls import path,include

from .views import *

urlpatterns=[
    path("",show_profile,name="profile"),

]