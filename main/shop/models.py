from django.db import models


class ReadyProduct(models.Model):
    name = models.CharField('Наименовение продукта', max_length=64)
    model = models.CharField('Модель продукта', max_length=64)
    selling_price_per_unit = models.IntegerField('Цена продажи за штуку')
    available_quantity = models.IntegerField('Количество на складе')
    picture = models.ImageField(upload_to='shoes/', default=None)

    class Meta:
        verbose_name = "Готовый продукт"
        verbose_name_plural = "Готовые продукты"
        ordering = ["id"]