from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from utils import check_user
from .models import *
from .forms import *
from user_profile.models import *
# Create your views here.

def play_video(req,id):
    res=check_user(req)
    if res:
        return res
    
    
    
    video=get_object_or_404(VideoModel,pk=id)
    selection=None
    is_pass=None
    is_teacher=True
    if Group.objects.get(name="teacher") not in req.user.groups.all():
        is_teacher=False
        try:
            selection=SelectionModel.objects.get(student=req.user,course=video.course)
            ProgressModel.objects.get(selection=selection,video=video)
            is_pass=True
        except SelectionModel.DoesNotExist:
            return redirect("/")
        except ProgressModel.DoesNotExist:
            is_pass=False
        
    if req.method=='POST':
        
        req.body
        if selection is not None:
            try:
                ProgressModel.objects.get(selection=selection,video=video)
            except ProgressModel.DoesNotExist:
                ProgressModel(selection=selection,video=video).save()
        
        return HttpResponse("pass" if selection is not None else "",content_type="text/plain")
        
    
    
    return render(req,"video/player.html",{"video":video,"pass":is_pass,"teacher":is_teacher})
    
def upload_video(req,cid):

    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
        
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Unknown user type")
    
    course=get_object_or_404(CourseModel,pk=cid)
    
    if course.teacher != req.user:
        raise Http404("User mismatch")
    
    if req.method=="POST" and req.FILES:
    
        base_name=str(course)+'_'
        print(base_name)
        for index, file in req.FILES.items():
            req.FILES[index].name=base_name+req.FILES[index].name
    
        form=VideoForm(req.POST,req.FILES)
        if form.is_valid():
            video=form.save(commit=False)
            
            video.course=course
            
            video.save()
            
            return redirect("/course/"+str(cid))
    else:
       form=VideoForm

    return render(req,"video/upload.html",{"form":form})
    
def delete_video(req,id):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
        
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Unknown user type")
        
    video=get_object_or_404(VideoModel,pk=id)
    
    path=video.source.storage
    name=video.source.name
    video.delete()
    
    #delete sourse file
    
    path.delete(name)
    
    return redirect(req.GET.get('next'))
