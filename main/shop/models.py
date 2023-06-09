from django.db import models

class Size(models.Model):
    size = models.IntegerField('Размер')

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"
        ordering = ["id"]

    def __str__(self):
        return str(self.size)
    
class Type(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
        ordering = ["id"]

    def __str__(self):
        return self.name

class ReadyProduct(models.Model):
    type = models.ForeignKey(Type, verbose_name='Тип', max_length=64, blank=True, null=True, on_delete=models.CASCADE)
    model = models.CharField('Модель', max_length=64)
    description = models.CharField('Описание', max_length=640)
    collection = models.CharField('Коллекция', max_length=64, default='-ytn-')
    selling_price_per_unit = models.IntegerField('Цена продажи за штуку')
    available_quantity = models.IntegerField('Количество на складе')
    color = models.CharField('Цвет', max_length=64)
    size = models.ManyToManyField(Size, verbose_name='Размер')
    picture = models.ImageField(upload_to='shoes/', default=None)

    class Meta:
        verbose_name = "Готовый продукт"
        verbose_name_plural = "Готовые продукты"
        ordering = ["id"]