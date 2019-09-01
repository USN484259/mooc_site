from django.shortcuts import render,get_object_or_404,redirect,Http404
#from django.core.exceptions import ObjectDoesNotExist
from utils import check_user
from .models import *
from course.models import *
from .forms import *

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
    
    #course=exam.course
    
    if Group.objects.get(name="student") in group :
        return detail_student(req,exam)
    if Group.objects.get(name="teacher") in group :
        return detail_teacher(req,exam)

    raise Http404("Unknown user type")


def exam_student(req,course):

    selection=get_object_or_404(SelectionModel,student=req.user,course=course)
    
    exams=ExamModel.objects.filter(course=course)
        
    for exam in exams:
        try:
            score=ScoreModel.objects.get(selection=selection,exam=exam)
            exam.result=score
            
        except ScoreModel.DoesNotExist:
            exam
        
    return render(req,"exam/student.html",{"course":course,"exams":exams})
    
def exam_teacher(req,course):
    
    if course.teacher!=req.user: raise Http404("User mismatch")

    exams=ExamModel.objects.filter(course=course)
    
    return render(req,"exam/teacher.html",{"course":course,"exams":exams})
    
def detail_student(req,exam):
    
    selection=get_object_or_404(SelectionModel,student=req.user,course=exam.course)
    
    try:
        ScoreModel.objects.get(selection=selection,exam=exam)
        raise Http404("Exam already taken")
        
    except ScoreModel.DoesNotExist:
        exam
    
    if req.method=="POST":
        form=ScoreForm(req.POST)
        if form.is_valid():
            score=form.save(commit=False)
            score.exam=exam
            score.total=exam.score
            score.selection=selection
            
            score.save()
            
            return redirect(exam_list,exam.course.pk)
            
    else:
        form=ScoreForm()
        
    return render(req,"exam/detail_student.html",{"exam":exam,"form":form})
    
    raise Http404("Not implemented")
    
    
def detail_teacher(req,exam):

    return render(req,"exam/detail_teacher.html",{"exam":exam})


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

