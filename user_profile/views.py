from django.shortcuts import render

from utils import check_user
from .models import *

# Create your views here.


def show_profile(req):
    res=check_user(req)
    if res:
        return res
    
    #TODO   teacher/student profiles
    return render(req,"profile/student.html")