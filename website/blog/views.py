from django.shortcuts import render,redirect,HttpResponse
import requests
from .models import Post
# Create your views here.


def blogHome(request):
    response=requests.get('http://127.0.0.1:8000/api/get_posts').json()
    return render(request,'blog/blogHome.html',{'posts':response})

def addPost(request):
    if request.method=="POST":

        title=request.POST.get("title")
        description=request.POST.get("description")
        print(title,description)
        data={'title':title,'description':description}

        response = requests.post('http://127.0.0.1:8000/api/add_post', data=data)
        return redirect('/')
    return render(request,'blog/addPost.html')


def viewPost(request,pk):

    response=requests.get('http://127.0.0.1:8000/api/view_post/'+pk).json()
    return render(request,'blog/postDetails.html',{'post':response})


def addComment(request,pk):
    if request.method=="POST":
        
        comment_body=request.POST.get("comment-body")
        post=Post.objects.get(id=pk)
        print(comment_body,post)
        data={'body':comment_body,'post':post}

        response = requests.post('http://127.0.0.1:8000/api/add_comment', data=data)
        print(response)
        return redirect('/')

def getComments(request,pk):

    # payload={'post_id':pk}

    response=requests.get('http://127.0.0.1:8000/api/get_comments/',params={"pk":pk}).json()
    return HttpResponse(response)

    


