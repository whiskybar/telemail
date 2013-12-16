from django.db import models


def encode_password(plain):
    return plain #TODO

class PasswordCharField(models.CharField):
    def save_form_data(self, instance, data):
        if data != u'':
            setattr(instance, self.name, encode_password(data))


