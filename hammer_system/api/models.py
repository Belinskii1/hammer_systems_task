from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=25,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Псевдоним'
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='Адрес почты'
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
