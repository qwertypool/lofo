from django.contrib import admin
from blogapp.models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=['status','author',]
    prepopulated_fields={'slug':('title',)}
    search_fields=('title',)
    date_hierarchy='publish'

class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','email','body','created','updated','active']
    list_filter=['active','created','updated']
    search_fields=('name','email','body')



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)