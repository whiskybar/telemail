from django.db import models


class DomainTrash(models.Model):
    domain = models.CharField(max_length=80, unique=True)
    trash = models.EmailField(max_length=254, verbose_name='default email')
    
    class Meta:
        ordering = ['domain']
        verbose_name_plural = 'domain trash'

    def __unicode__(self):
        return '%s -> %s' % (self.domain, self.trash)

