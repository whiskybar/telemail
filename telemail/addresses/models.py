from django.db import models
from django.utils.translation import ugettext_lazy as _
from telemail.addresses.fields import PasswordCharField


class Account(models.Model):
    address = models.EmailField(max_length=254, unique=True, verbose_name=_('address'))
    password = PasswordCharField(max_length=130, blank=True, verbose_name=_('password'), help_text=_('leave blank for no change'))

    class Meta:
        ordering = ['address']
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def __unicode__(self):
        return self.address


class Alias(models.Model):
    address = models.EmailField(max_length=254, unique=True, verbose_name=_('address'))

    class Meta:
        ordering = ['address']
        verbose_name = _('alias')
        verbose_name_plural = _('aliases')

    def __unicode__(self):
        return '%s = %s' % (self.address, ', '.join(unicode(d) for d in self.aliases.all()))

class Other(models.Model):
    origin = models.ForeignKey(Alias, related_name='aliases')
    alias = models.CharField(max_length=254, verbose_name=_('address'))

    class Meta:
        ordering = ['alias']

    def __unicode__(self):
        return self.alias

class Forward(models.Model):
    address = models.EmailField(max_length=254, unique=True, verbose_name=_('address'))

    class Meta:
        ordering = ['address']
        verbose_name = _('forward')
        verbose_name_plural = _('forwards')

    def __unicode__(self):
        return '%s -> %s' % (self.address, ', '.join(unicode(d) for d in self.destinations.all()))

class ForwardedAddress(models.Model):
   source = models.ForeignKey(Forward, related_name='destinations')
   destination = models.EmailField(max_length=254, verbose_name=_('address'))

   class Meta:
       ordering = ['destination']

   def __unicode__(self):
       return self.destination
