from django.db import models

# Create your models here.
class employee(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=60)
    empsal=models.IntegerField()
    empaddr=models.CharField(max_length=60)