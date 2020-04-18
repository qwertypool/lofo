from blogapp.models import Post
from django import template
register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count() 

@register.inclusion_tag('blogapp/latest.html')
def show_posts():
    latest_post=Post.objects.order_by('-publish')[:5]
    return{'latest_post':latest_post}

from django.db.models import Count

# @register.inclusion_tag('blogapp/base.html')
# def total_comments():
#     most_commented=Post.objects.Count('comments').order_by('-most_commented')
#     return {'most_commented':most_commented}




# @register.assignment_tag
# def total_comments(count=5):
#     return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')

# @register.assignment_tag
#   def any_function(count=5):
#       return *some database query*