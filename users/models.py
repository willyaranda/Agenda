from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()
    notes = models.TextField()
    website = models.URLField()
    nickname = models.TextField()