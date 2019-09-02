from django.urls import path
from .views import *

# start with blog
urlpatterns = [
	path("<int:cid>", exam_list, name = 'exam_list'),
    path("new/<int:cid>",exam_new,name="new_exam"),
    path("statistics/<int:cid>",exam_statistics,name="exam_statistics"),
    path("exam/<int:eid>",exam_detail,name="exam_detail"),
    path("check/<int:sid>",exam_check,name="check_answer"),
]
