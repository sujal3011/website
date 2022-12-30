from django.shortcuts import render

# Create your views here.


def blogHome(request):
    return render(request,'blog/blogHome.html')

def addPost(request):
    return render(request,'blog/addPost.html')

