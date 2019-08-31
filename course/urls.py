from django.urls import path,include

from .views import *

urlpatterns=[
    path("<int:id>/",show_course,name='course_list'),
    path("select/<int:id>/",select_course),
    path("deselect/<int:id>/",deselect_course),
    path("create/",create_course,name="create_course"),
]