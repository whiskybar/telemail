from django.db import models


class NoSpamHost(models.Model):
    host = models.CharField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['host']
        verbose_name = 'ignored host'

    def __unicode__(self):
        return self.host


class NoSpamRecipient(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    
    class Meta:
        ordering = ['address']
        verbose_name = 'ignored address'
        verbose_name_plural = 'ignored addresses'

    def __unicode__(self):
        return self.address


class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['subject']
        
    def __unicode__(self):
        return self.subject


