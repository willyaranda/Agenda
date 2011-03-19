from django.db import models
#from users.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    #users = models.ManyToManyField(User)