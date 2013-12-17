import random
import crypt
from passlib.hash import sha512_crypt
from django.db import models


def encode_password(plain):
    return sha512_crypt.encrypt(plain, rounds=5000)

class PasswordCharField(models.CharField):
    def save_form_data(self, instance, data):
        if data != u'':
            setattr(instance, self.name, encode_password(data))


