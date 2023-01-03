from django.contrib import admin
from .models import Post,Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','description','created_at','updated_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','body','post','created_at','updated_at']
