from django.urls import path
from .views import *

# start with blog
urlpatterns = [
	path("<int:cid>", exam_list, name = 'exam_list'),
    path("exam/<int:eid>",exam_detail,name="exam_detail"),
    path("new/<int:cid>",exam_new,name="new_exam"),
]
