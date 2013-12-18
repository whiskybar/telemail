from django.db import models
from django.utils.translation import ugettext_lazy as _


class DomainTrash(models.Model):
    domain = models.CharField(max_length=80, unique=True, verbose_name=_('domain'))
    trash = models.EmailField(max_length=254, verbose_name=_('default email'))
    
    class Meta:
        ordering = ['domain']
        verbose_name = _('domain trash')
        verbose_name_plural = _('domain trashes')

    def __unicode__(self):
        return '%s -> %s' % (self.domain, self.trash)

