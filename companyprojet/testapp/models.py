from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 150)
    ceo = models.CharField(max_length = 150)
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})