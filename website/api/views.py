from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post,Comment
from rest_framework import viewsets
from .serializers import PostSerializer,CommentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[IsAdminUser]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class=CommentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]










# @api_view(['GET'])
# def getPosts(request):
#     posts=Post.objects.all()
#     serializer=PostSerializer(posts,many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addPost(request):
#     serializer=PostSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['GET'])
# def viewPost(request,pk):
#    posts=Post.objects.get(id=pk)
#    serializer=PostSerializer(posts,many=False)
#    return Response(serializer.data)


# @api_view(['POST'])
# def addComment(request):
#     serializer=CommentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['GET'])
# def getComments(request):
#     comments=Comment.objects.all()
#     serializer=CommentSerializer(comments,many=True)
#     return Response(serializer.data)










