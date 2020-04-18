from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.urls import reverse
from time import gmtime, strftime
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    STATUS=(('draft','Draft'),('published','Published'))
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique_for_date='publish')
    author= models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=0,null=True)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices=STATUS, default='draft')
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        kwargs = {'year': self.publish.year,
              'month': self.publish.strftime('%m').lower(),
              'day': self.publish.strftime('%d'),
              'post': self.slug,
                }
        return reverse("blogapp:post-details",args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.post)
   

    

    
    
    
    




'''
    class IsoDateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return str(value)


register_converter(IsoDateConverter, 'isodate')
    
'''
    
    