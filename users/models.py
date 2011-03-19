from django.db import models
from groups.models import Group

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
    #groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return u'%s %s' % (self.name) % (self.surname)