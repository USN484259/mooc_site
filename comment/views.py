from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment
from blog.models import *
from course.models import *
from user_profile.models import *
from utils import check_user


# Create your views here.
def update_comment(request,blog_id):
    res=check_user(request)
    if res:
        return res
    
    course=get_object_or_404(Blog,pk=blog_id).reference
    #course=get_object_or_404(CourseModel,pk=blog_id)
    
    if course.teacher!=request.user:
        get_object_or_404(SelectionModel,student=request.user,course=course)




    referer = request.META.get('HTTP_REFERER', reverse('index'))    
    user = request.user

    #数据检查
    # if not user.is_authenticated:
        # return render(request, 'error.html', {'message':'用户未登录', 'redirect_to':referer})

    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'message':'评论内容为空', 'redirect_to':referer})

    try:
        content_type = request.POST.get('content_type', '')
        #object_id = int(request.POST.get('object_id', ''))
        object_id=blog_id
        model_class = ContentType.objects.get(model = content_type).model_class()
        model_obj = model_class.objects.get(pk = object_id)
    except Exception as e:
        return render(request, 'error.html', {'message':'评论对象不存在', 'redirect_to':referer})

    #检查通过，保存数据
    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)