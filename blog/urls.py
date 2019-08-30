from django.urls import path
from . import views

# start with blog
urlpatterns = [
	#localhost:8000/blog/1
	#path('', views.blog_list, name = "blog_list"),
    path('detail/<int:blog_pk>', views.blog_detail, name = "blog_detail"),
    path('new/<int:id>',views.blog_new,name="blog_new"),
    path('<int:id>',views.blog_course,name="blog_list"),
    #path('type/<int:blog_type_pk>', views.blogs_with_type, name = "blogs_with_type"),
]
