from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPosts),
    path('add_post', views.addPost),
]