from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('post',views.PostViewSet,basename='post')
router.register('comment',views.CommentViewSet,basename='comment')



urlpatterns = [
    # path('get_posts', views.getPosts,name="getPosts"),
    # path('add_post', views.addPost,name="addPost"),
    # path('view_post/<str:pk>', views.viewPost,name="viewPost"),
    # path('add_comment', views.addComment,name="addComment"),
    # path('get_comments', views.getComments,name="getComments"),
    path('',include(router.urls)),
    path('auth',include('rest_framework.urls',namespace='rest_framework'))
]