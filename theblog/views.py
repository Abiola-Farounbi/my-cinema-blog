from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Category
from .forms import *

# Create your views here.
def homepage(request):
    posts=Post.objects.order_by('-id')
    categories = Category.objects.all()
    header="The_cinema"
    latest_post=Post.objects.order_by('-published')[:3]
    return render(request, "homepage.html", {"titles":posts,"header":header, 'category':categories,'latest_post':latest_post,})
def film_post(request):
    create=Postform
    form=create(request.POST or None)
    if request.method == 'POST':
       form= create(request.POST, request.FILES)
       if form.is_valid():
         # post=form.save(commit=False)
          #post.author=request.user
          form.save()
          return redirect('/theblog')
       else:
           form = Postform() 
    return render(request,'newpost.html' , {'form':form}) 
#def display_image(request):
 #   if request.method=='GET':
  #     display=Post.objects.all()
   #    return render(request, "test.html",{'display':display} )
def singlepage(request, post_id):
    post=Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request,'singlepost.html' , {'post':post, 'category':categories} )