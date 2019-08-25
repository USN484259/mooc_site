import os

from django.shortcuts import render,get_object_or_404,redirect
from utils import check_user
from .models import *
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
    
def upload_video(req):

    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
        
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Unknown user type")

    if req.method=="POST":
        form=VideoModel(req.POST)
        if form.is_valid():
            
            video=form.save()
        
    else:
        form=VideoModel
       

    return render(req,"video/upload.html",{"form":form})
    
def delete_video(req,id):
    res=check_user(req)
    if res:
        return res
    
    group=req.user.groups.all()
        
    if Group.objects.get(name="teacher") not in group :
        raise Http404("Unknown user type")
        
    video=get_object_or_404(VideoModel,pk=id)
    
    source=video.source
    
    video.delete()
    
    #delete sourse file
    os.remove(source)
    print("video file "+source+" deleted")
    
    return redirect(req.GET.get('next'))
