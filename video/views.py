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
    
    if not SelectionModel.objects.filter(student=req.user,course=video.course):
        return redirect("/")
    
    return render(req,"video/player.html",{"name":video.name,"source":video.source})