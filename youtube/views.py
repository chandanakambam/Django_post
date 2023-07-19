from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    #print(posts)
    return render( request, 'index.html',context={'posts':posts})

def about(request):
    return render(request,'about.html')