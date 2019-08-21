from django.shortcuts import render

# Create your views here.

def register(req):
    return render(req,"registration/register.html")

