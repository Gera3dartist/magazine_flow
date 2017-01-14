import binascii
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
import os
from django.db import models
from django.contrib.auth.hashers import check_password, make_password

_app_label = 'core'


class CoreBaseUser(models.Model):
    email = models.CharField(max_length=256, unique=True)
    password = models.CharField('password', max_length=128)
    created = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = _app_label
        abstract = True

    def is_authenticated(self):
        return True

    def check_password(self, password):
        return check_password(password, self.password)

    def set_password(self, password):
        self.password = make_password(password)

    def save(self, *args, **kwargs):
        if not self.check_password(self.password):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class TokenModel(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = _app_label
        abstract = True

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(TokenModel, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()
