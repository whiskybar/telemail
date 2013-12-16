import random
import crypt
from django.db import models


CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789./'
def encode_password(plain):
    return crypt.crypt('plain', '$6$%s$' % ''.join(random.choice(CHARSET) for _ in xrange(16)))

class PasswordCharField(models.CharField):
    def save_form_data(self, instance, data):
        if data != u'':
            setattr(instance, self.name, encode_password(data))


