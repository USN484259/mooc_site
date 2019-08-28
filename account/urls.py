from django.urls import path,include
from . import views

# from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm

urlpatterns=[
    # path("register",CreateView.as_view(
            # template_name='registration/register.html',
            # form_class=UserCreationForm,
            # success_url='/'
    # ),name="register"),
    
    #path("login/",views.login,name="login"),
    #path("logout/",views.logout,name="logout"),
    
    path("register/",views.register,name="register"),
    path("reg_teacher/",views.reg_teacher,name="reg_teacher"),
    path("success/<teacher>",views.success,name="reg_success"),
    path("",include('django.contrib.auth.urls')),
]