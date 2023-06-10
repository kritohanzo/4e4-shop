from django.db import models
from django.contrib.auth.models import AbstractUser
from core.confirm_code_generator import generate_code

class User(AbstractUser):
    # username = models.CharField(max_length=64, null=True, unique=False, blank=True)
    email = models.CharField('Почта', max_length=32)
    confirm_code = models.IntegerField('Код подтверждения', default=generate_code())
    confirmed = models.BooleanField('Подтверждено', default=False)
    worker = models.BooleanField('Работник', default=False)
    active_orders = models.IntegerField('Активные заказы', default=0)

    @property
    def is_confirmed(self):
        return self.confirmed
    
    @property
    def is_worker(self):
        return self.worker

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["id"]