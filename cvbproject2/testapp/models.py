from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150)
    page = models.IntegerField()
    price = models.FloatField()
    
    
    
    