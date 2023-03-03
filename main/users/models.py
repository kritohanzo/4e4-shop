from django.db import models

# Create your models here.

class Worker(models.Model):
    name_surname = models.CharField('Работник', max_length=64)
    number = models.CharField('Номер телефона', max_length=11)
    password = models.CharField('Пароль', max_length=16, default='123456')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ["id"]