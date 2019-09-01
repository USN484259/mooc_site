from django.shortcuts import render,get_object_or_404,redirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from utils import check_user
from .models import *
from course.models import *
#from .forms import *
# Create your views here.

def exam_list(req,cid):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
    
    course=get_object_or_404(CourseModel,pk=cid)
    
    if Group.objects.get(name="student") in group :
        return exam_student(req,course)
    if Group.objects.get(name="teacher") in group :
        return exam_teacher(req,course)

    raise Http404("Unknown user type")

def exam_detail(req,eid):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
    
    exam=get_object_or_404(ExamModel,pk=eid)
    
    course=exam.course
    
    if Group.objects.get(name="student") in group :
        return detail_student(req,course)
    if Group.objects.get(name="teacher") in group :
        return detail_teacher(req,course)

    raise Http404("Unknown user type")


def exam_student(req,course):

    get_object_or_404(SelectionModel,student=req.user,course=course)

    exams=ExamModel.objects.filter(course=course)
    for exam in exams:
        try:
            selection=SelectionModel.objects.get(student=req.user)
            exam.score=ScoreModel.objects.get(selection=selection,exam=exam)
        except ObjectDoesNotExist:
            exam
        
    return render(req,"exam/student.html",{"course":course,"exams":exams})
    
def exam_teacher(req,course):
    
    if course.teacher!=req.user: raise Http404("User mismatch")

    exams=ExamModel.objects.filter(course=course)
    
    return render(req,"exam/teacher.html",{"course":course,"exams":exams})
    
def detail_student(req,course):
    raise Http404("Not implemented")
    
    
def detail_teacher(req,course):
    raise Http404("Not implemented")

def exam_new(req,cid):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
    
    course=get_object_or_404(CourseModel,pk=cid)
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Invalid user group")

    if req.method=="POST":
        form=ExamForm(req.POST)
        if form.is_valid():
            exam=form.save(commit=False)
            exam.course=course
            
            exam.save()
            
            return redirect(exam_list,course.pk)
            
        
    else:
        form=ExamForm()

    return render(req,"exam/exam_new.html",{"form":form})

