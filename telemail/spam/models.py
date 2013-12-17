from django.db import models


class NoSpamHost(models.Model):
    host = models.CharField(max_length=200, unique=True, help_text="sending host not checked for spam")
    
    class Meta:
        ordering = ['host']
        verbose_name = 'trusted host'

    def __unicode__(self):
        return self.host


class NoSpamRecipient(models.Model):
    address = models.EmailField(max_length=254, unique=True, help_text="address not checked for spam")
    
    class Meta:
        ordering = ['address']
        verbose_name = 'whitelist address'
        verbose_name_plural = 'whitelist addresses'

    def __unicode__(self):
        return self.address


class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True, help_text="considered spam")
    
    class Meta:
        ordering = ['subject']
        
    def __unicode__(self):
        return self.subject


