from django.db import models

# Create your models here.
class Employee(models.Model):
    enum = models.IntegerField()
    ename = models.CharField(max_length = 150)
    esal = models.FloatField()
    eaddr = models.CharField(max_length = 256)
    
    def __str__(self):
        return self.ename
    
    
class Company(models.Model):
    cnum = models.IntegerField()
    cname = models.CharField(max_length = 150)
    clocation = models.CharField(max_length = 150)
    
    
        