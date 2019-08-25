from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns=[
    path("<int:id>/",play_video),
    path("upload/<int:cid>/",upload_video),
    path("delete/<int:id>/",delete_video),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)