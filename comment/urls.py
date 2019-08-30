from django.urls import path
from . import views

# start with blog
urlpatterns = [
	path("update_comment/<int:blog_id>", views.update_comment, name = 'update_comment')
]
