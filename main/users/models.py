from django.db import models
from django.contrib.auth import get_user_model


class Worker(models.Model):
    name_surname = models.CharField('Работник', max_length=64)
    number = models.CharField('Номер телефона', max_length=16)
    password = models.CharField('Пароль', max_length=16, default='123456')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ["id"]

class User(models.Model):
    name_surname = models.CharField('Покупатель', max_length=64)
    email = models.CharField('Почта', max_length=32)
    password = models.CharField('Пароль', max_length=16, default='123456')
    confirm_code = models.IntegerField('Код подтверждения')
    confirmed = models.BooleanField('Подтверждено', default=False)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ["id"]