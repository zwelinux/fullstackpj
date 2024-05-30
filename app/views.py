from django.shortcuts import render
from .models import Blog 

def home(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs' : blogs
    }
    return render(request, 'app/home.html', context)