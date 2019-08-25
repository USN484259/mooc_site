from django.shortcuts import render,get_object_or_404
from django.http import Http404

from utils import check_user
from .models import *
from course.models import *

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
    list=[]
    try:
        selection=SelectionModel.objects.filter(student=req.user)
        for item in selection:
            list.append(item.course)
            
    except SelectionModel.DoesNotExist:
        list=None
    except CourseModel.DoesNotExist:
        list=None
    
    return render(req,"profile/student.html",{"courses":list})
    
    
def show_teacher(req):

    courses=CourseModel.objects.filter(teacher=req.user)
    
    for item in courses:
        item.count=len(SelectionModel.objects.filter(course=item))

    return render(req,"profile/teacher.html",{"courses":courses})

def selection(req):
    selected_list=set()
    try:
        
        for item in set(SelectionModel.objects.filter(student=req.user)):
            selected_list.add(item.course)
            
    except SelectionModel.DoesNotExist:
        selected_list
    
    return render(req,"profile/selection.html",{"courses":set(CourseModel.objects.all())-selected_list})
