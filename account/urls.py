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
    path("register",views.register,name="register"),
    path("",include('django.contrib.auth.urls')),
]