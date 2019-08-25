from django.shortcuts import render,get_object_or_404,redirect
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
    
    if req.user.groups.filter(name="teacher") or SelectionModel.objects.filter(student=req.user,course=video.course):
        req
    else:
        return redirect("/")
    
    return render(req,"video/player.html",{"name":video.name,"source":video.source})
    
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
