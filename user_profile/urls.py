from django.urls import path,include

from .views import *

urlpatterns=[
    path("select/",selection,name="selection"),
    path("",show_profile,name="profile"),

]