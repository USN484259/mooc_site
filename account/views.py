from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group

# Create your views here.

def register(req):
    if req.method=="POST":
        form=UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name="student")
            user.groups.add(group)
            return redirect("/")
    else:  
        form=UserCreationForm
        
        
    return render(req,"registration/register.html",{"form":form})

