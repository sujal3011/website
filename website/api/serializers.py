from rest_framework import serializers
from blog.models import Post,Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','body','post','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):
    comment=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields=['id','title','description','created_at','updated_at','comment']

