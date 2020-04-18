from django.db import models

# Create your models here.
class Adhar(models.Model):
    id="Adhar"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()
    
class VoterId(models.Model):
    id="Voter"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()

class Passport(models.Model):
    id="Passport"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()

class Atm(models.Model):
    id="Atm"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()

class Pan(models.Model):
    id="Pan"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()

class Fadhar(models.Model):
    id="Fadhar"
    name = models.CharField(max_length = 150)
    uid = models.IntegerField()