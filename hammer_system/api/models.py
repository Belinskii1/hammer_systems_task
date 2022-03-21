from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

from django.conf import settings


class User(AbstractUser):
    username = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        verbose_name='Псевдоним'
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Имя пользователя'
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Фамилия'
    )
    telephone_number = models.CharField(
        max_length=11,
        blank=True,
        unique=True,
        verbose_name='номер телефона'
    )

    USERNAME_FIELD = 'telephone_number'
    REQUIRED_FIELDS = ('username',)


def generate_activation_code():
    return ''.join([random.choice(list('123456789')) for x in range(4)])


class ActivationCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    code = models.CharField(max_length=4, default=generate_activation_code)


def generate_invite_code():
    return ''.join([random.choice(list(string.ascii_uppercase + string.digits)) for x in range(6)])




class InviteCode(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Псевдоним'
    )
    invite_code = models.CharField(
        max_length=6,
        default=generate_invite_code,
        verbose_name='код приглашения'
    )
