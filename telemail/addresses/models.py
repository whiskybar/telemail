from django.db import models
from telemail.addresses.fields import PasswordCharField


class Account(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    password = PasswordCharField(max_length=130, blank=True, help_text='leave blank for no change')
    
    class Meta:
        ordering = ['address']

    def __unicode__(self):
        return self.address


class Alias(models.Model):
    address = models.EmailField(max_length=254, unique=True, verbose_name='address')
    
    class Meta:
        ordering = ['address']
        verbose_name_plural = 'aliases'

    def __unicode__(self):
        return '%s = %s' % (self.address, ', '.join(unicode(d) for d in self.aliases.all()))

class Other(models.Model):
    origin = models.ForeignKey(Alias, related_name='aliases')
    alias = models.EmailField(max_length=254, verbose_name='address')

    class Meta:
        ordering = ['alias']

    def __unicode__(self):
        return self.alias

class Forward(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    
    class Meta:
        ordering = ['address']

    def __unicode__(self):
        return '%s -> %s' % (self.address, ', '.join(unicode(d) for d in self.destinations.all()))

class ForwardedAddress(models.Model):
   source = models.ForeignKey(Forward, related_name='destinations')
   destination = models.EmailField(max_length=254, verbose_name='address')

   class Meta:
       ordering = ['destination']

   def __unicode__(self):
       return self.destination
