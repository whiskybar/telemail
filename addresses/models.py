from django.db import models
from addresses.fields import PasswordCharField


class Account(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    password = PasswordCharField(max_length=130, blank=True, help_text='leave blank for no change')
    
    class Meta:
        ordering = ['address']

    def __unicode__(self):
        return self.address

