from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)


def blogPost(request,slug):
    return render(request,'blog/blogPost.html')

   