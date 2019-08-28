from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group

# Create your views here.

# def login(req):
    # if req.is_authenticated:
        # auth.logout(req)
    
    # if req.method=="POST":
        # form=LoginForm(req.POST)
        # if form.is_valid():
            # user=form.cleaned_data["user"]
            # auth.login(req,user)
            # return redirect(req.GET.get('next'))
    
    # else:
        # form=LoginForm()

    # return render(req,"account/login.html",{"form":form})



def register(req):
    if req.method=="POST":
        form=UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name="student")
            user.groups.add(group)
            return redirect("../success/student")
    else:  
        form=UserCreationForm
        
        
    return render(req,"registration/register.html",{"form":form})

def reg_teacher(req):
    if req.method=="POST":
        form=UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            user.is_active=False;
            group=Group.objects.get(name="teacher")
            user.groups.add(group)
            user.save()
            return redirect("../success/teacher")
    else:  
        form=UserCreationForm
        
        
    return render(req,"registration/reg_teacher.html",{"form":form})


def success(req,teacher=None):
        
        return render(req,"registration/success.html",{"teacher":True if teacher=="teacher" else False})
        
        