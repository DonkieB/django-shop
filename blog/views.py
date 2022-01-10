from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404

def post_list(request):
    blogs = Blog.objects.all()
    return render(request, './blog-overzicht.html', {'blogs': blogs})

def blog(request):
    return HttpResponse('Blog detail!')