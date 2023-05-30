from django.db import models
from django.contrib.auth.models import AbstractUser


class Worker(models.Model):
    name_surname = models.CharField('Работник', max_length=64)
    number = models.CharField('Номер телефона', max_length=16)
    password = models.CharField('Пароль', max_length=16, default='123456')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ["id"]

class User(AbstractUser):
    # username = models.CharField(max_length=64, null=True, unique=False, blank=True)
    email = models.CharField('Почта', max_length=32)
    confirm_code = models.IntegerField('Код подтверждения', null=True)
    confirmed = models.BooleanField('Подтверждено', default=False)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ["id"]