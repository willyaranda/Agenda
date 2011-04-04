from django.db import models

# l10n
from django.utils.translation import ugettext_lazy as _

class Group(models.Model):
    name = models.CharField(_("Group"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Person(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), help_text=_("A small identifier for the person"))
    surname = models.CharField(_("Surname"), max_length=50)
    phone = models.IntegerField(_("Phone"), blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    birthday = models.DateField(_("Birthday"), blank=True, null=True)
    notes = models.TextField(_("Notes"), blank=True, null=True)
    website = models.URLField(_("URL"), blank=True, null=True, help_text=_("Home page of the person"))
    nickname = models.CharField(_("Nickname"), max_length=50, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)