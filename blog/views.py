from django.shortcuts import render_to_response, get_object_or_404, render
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType

from .models import Blog, BlogType
from comment.models import Comment

def blog_list(request):
	blogs_all_list = Blog.objects.all()
	page_num = request.GET.get('page',1) #获取url的页面参数（GET请求）
	paginator = Paginator(blogs_all_list,10)	#每10页进行分页
	page_of_blogs = paginator.get_page(page_num)	# 自动识别页码符号以及无效处理

	context = {}
	context['page_of_blogs'] = page_of_blogs
	context['blog_types'] = BlogType.objects.all()
	context['blogs_count'] = Blog.objects.all().count()
	return render(request, 'blog/blog_list.html', context)

def blog_detail(request, blog_pk):
	blog = get_object_or_404(Blog, pk = blog_pk)
	blog_content_type = ContentType.objects.get_for_model(blog)
	comments = Comment.objects.filter(content_type = blog_content_type, object_id = blog.pk)

	context = {}
	context['blog'] = blog
	context['user'] = request.user
	context['comments'] = comments
	response = render(request, 'blog/blog_detail.html', context) # 响应
	return render(request, 'blog/blog_detail.html', context)

def blogs_with_type(request, blog_type_pk):
	context = {}
	blog_type = get_object_or_404(BlogType, pk = blog_type_pk)
	context['blog_type'] = blog_type
	context['blogs'] = Blog.objects.filter(blog_type = blog_type)
	context['blog_types'] = BlogType.objects.all()
	return render(request, 'blog/blogs_with_type.html', context)
