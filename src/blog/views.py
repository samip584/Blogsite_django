from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.utils import timezone
from .forms import BlogPostModelForm

# Create your views here.

def blog_post_detail_view(request, slug):
	obj = get_object_or_404(BlogPost, slug = slug )
	template_name = 'blog/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)


def blog_post_list_page(request):
	#lists out objects
	#could search
	qs = BlogPost.objects.all().published()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user = request.user)
		qs = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = {"object_list": qs}
	return render(request, template_name, context)


def blog_post_search_page(request):
	#lists out objects
	#could search
	qs = BlogPost.objects.filter(title__icontains='Hello')
	template_name = 'blog/list.html'
	context = {"object_list": qs}
	return render(request, template_name, context)

@staff_member_required
#@login_required
def blog_post_create_page(request):
	#creates objects
	form = BlogPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = BlogPostModelForm()
	template_name = 'blog/create.html'
	context = {"form": form}
	return render(request, template_name, context)

@staff_member_required
#@login_required
def blog_post_update_page(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'form.html'
	context = {"title": f"Update {obj.title}", "form": form}
	return render(request, template_name, context)  

@staff_member_required
#@login_required
def blog_post_delete_page(request, slug):
	obj = get_object_or_404(BlogPost, slug = slug )
	template_name = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return	redirect("/blog")
	context = {"object": obj}
	return render(request, template_name, context)