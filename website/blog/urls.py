from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome,name="blogHome"),
    path('add_post', views.addPost,name="addPost"),
    path('view_post/<str:pk>', views.viewPost,name="viewPost"),
    path('add_comment/<str:pk>', views.addComment,name="addComment"),
    path('get_comments/<str:pk>', views.getComments,name="getComments"),
]