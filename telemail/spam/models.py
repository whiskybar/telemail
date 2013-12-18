from django.db import models
from django.utils.translation import ugettext_lazy as _


class NoSpamHost(models.Model):
    host = models.CharField(max_length=200, unique=True, verbose_name=_('host'), help_text=_("sending host not checked for spam"))
    
    class Meta:
        ordering = ['host']
        verbose_name = _('trusted host')
        verbose_name_plural = _('trusted hosts')

    def __unicode__(self):
        return self.host


class NoSpamRecipient(models.Model):
    address = models.EmailField(max_length=254, unique=True, verbose_name=_('address'), help_text=_("address not checked for spam"))
    
    class Meta:
        ordering = ['address']
        verbose_name = _('whitelisted address')
        verbose_name_plural = _('whitelisted addresses')

    def __unicode__(self):
        return self.address


class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True, verbose_name=_('subject'), help_text=_("considered spam"))
    
    class Meta:
        ordering = ['subject']
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')
        
    def __unicode__(self):
        return self.subject


