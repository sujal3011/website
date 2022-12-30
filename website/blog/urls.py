from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome),
    path('add_post', views.addPost),
]