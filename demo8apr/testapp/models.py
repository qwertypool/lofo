from django.db import models

# Create your models here.
class Myself(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    proffession = models.CharField(max_length = 150)
    
    
class Enemies(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    proffession = models.CharField(max_length = 150)
    
    
class Demo(models.Model):
    subject = models.CharField(max_length = 150)
    marks = models.IntegerField()
    
    