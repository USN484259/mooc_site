from django.shortcuts import render,get_object_or_404,redirect

from utils import check_user
from .models import *
from video.models import *

# Create your views here.

def show_course(req,id):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
    
    course=get_object_or_404(CourseModel,pk=id)
    
    if Group.objects.get(name="student") in group :
        return show_student(req,course)
    if Group.objects.get(name="teacher") in group :
        return show_teacher(req,course)

    raise Http404("Unknown user type")

def show_student(req,course):
    videos=[]
    try:
        videos=VideoModel.objects.filter(course=course)
    except VideoModel.DoesNotExist:
        videos=None
    
    selected=SelectionModel.objects.filter(student=req.user,course=course)
    
    return render(req,"course/student.html",{"course":course,"videos":videos,"selected":True if selected else False})
    
def show_teacher(req,course):
    videos=[]
    try:
        videos=VideoModel.objects.filter(course=course)
    except VideoModel.DoesNotExist:
        videos=None

    return render(req,"course/teacher.html",{"course":course,"videos":videos})
    
    
def select_course(req,id):
    res=check_user(req)
    if res:
        return res
    group=req.user.groups.all()
        
    if Group.objects.get(name="student") not in group :
        raise Http404("Unknown user type")    
    
    course=get_object_or_404(CourseModel,pk=id)
    selection=SelectionModel.objects.filter(student=req.user,course=course)
    
    if not selection:
        SelectionModel(student=req.user,course=course).save()
        
        
    return redirect(req.GET.get('next'))

def deselect_course(req,id):
    res=check_user(req)
    if res:
        return res
    group=req.user.groups.all()
        
    if Group.objects.get(name="student") not in group :
        raise Http404("Unknown user type")  

        
    course=get_object_or_404(CourseModel,pk=id)
    SelectionModel.objects.filter(student=req.user,course=course).delete()

    return redirect(req.GET.get('next'))


def create_course(req):
    return render(req,"course/new_course.html")