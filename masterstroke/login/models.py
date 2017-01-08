from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model) :
    first_name = models.CharField(max_length=500)
    username = models.CharField(max_length=100, unique = True)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    phone_number = models.IntegerField(max_length = 20)
    address = models.CharField(max_length = 500)

class homeDetails(models.Model) :
    name =  models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=500)
    owner = models.ForeignKey(User)
    cost = models.IntegerField(null = True, blank = True)
    schoolNearby = models.CharField(max_length=100)
    gardenNearby = models.CharField(max_length=100)
    marketNearby = models.CharField(max_length=100)
