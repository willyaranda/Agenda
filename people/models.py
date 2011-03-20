from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()
    notes = models.TextField()
    website = models.URLField()
    nickname = models.CharField(max_length=50)
    groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return u'%s' % (self.name)