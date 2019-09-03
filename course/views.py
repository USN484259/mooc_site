from django.shortcuts import render,get_object_or_404,redirect,Http404

from utils import check_user
from .models import *
from video.models import *
from .forms import *

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
    videos=VideoModel.objects.filter(course=course)
    try:
        selection=SelectionModel.objects.get(student=req.user,course=course)
        
        progress={"current":ProgressModel.objects.filter(selection=selection).count(),"total":VideoModel.objects.filter(course=course).count()}
        
    except SelectionModel.DoesNotExist:
        progress=None
    
    return render(req,"course/student.html",{"course":course,"videos":videos,"progress":progress})
    
def show_teacher(req,course):
    videos=VideoModel.objects.filter(course=course)

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
    res=check_user(req)
    if res:
        return res
    group=req.user.groups.all()
    
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Unknown user type")  

    if req.method=="POST":
        form=CourseForm(req.POST)
        if form.is_valid():
            
            course=form.save(commit=False)
            
            course.teacher=req.user
            
            course.save()
            
            return redirect("/profile")
    
    else:
        form=CourseForm
    

    return render(req,"course/new_course.html",{"form":form})