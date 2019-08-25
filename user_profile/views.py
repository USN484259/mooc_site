from django.shortcuts import render,get_object_or_404
from django.http import Http404

from utils import check_user
from .models import *

# Create your views here.


def show_profile(req):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
    
    if Group.objects.get(name="student") in group :
        return show_student(req)
    if Group.objects.get(name="teacher") in group :
        return show_teacher(req)

    raise Http404("Unknown user type")
    
    
def show_student(req):
    course=[]
    try:
        selection=SelectionModel.objects.filter(student=req.user)
        for item in selection:
            course.append(item.course)
            
    except SelectionModel.DoesNotExist:
        course=None
    except CourseModel.DoesNotExist:
        course=None
    
    return render(req,"profile/student.html",{"courses":course})
    
    
def show_teacher(req):
    return render(req,"profile/teacher.html")

