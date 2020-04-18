from django.db import models

# Create your models here.
class adhar(models.Model):
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()
    