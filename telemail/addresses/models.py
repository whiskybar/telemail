from django.db import models
from addresses.fields import PasswordCharField


class Account(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    password = PasswordCharField(max_length=130, blank=True, help_text='leave blank for no change')
    
    class Meta:
        ordering = ['address']

    def __unicode__(self):
        return self.address


class Alias(models.Model):
    source = models.EmailField(max_length=254, unique=True)
    destination = models.EmailField(max_length=254)
    
    class Meta:
        ordering = ['source']
        verbose_name_plural = 'aliases'

    def __unicode__(self):
        return '%s -> %s' % (self.source, self.destination)


class Forward(models.Model):
    source = models.EmailField(max_length=254, unique=True)
    destination = models.EmailField(max_length=254, help_text='comma separated addesses')
    
    class Meta:
        ordering = ['source']

    def __unicode__(self):
        return '%s -> %s' % (self.source, self.destination)
