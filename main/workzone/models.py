from django.db import models
from users.models import User
from shop.models import ReadyProduct, Size, Type
from users.models import User

class Provider(models.Model):
    name = models.CharField("Наименование поставщика", max_length=64)
    number = models.CharField("Номер телефона", max_length=16)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Наименование продукта", max_length=64)
    purchase_price_per_unit = models.IntegerField("Цена закупки за штуку")
    available_quantity = models.IntegerField("Количество на складе")
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Поставщик",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]

    def __str__(self):
        return self.name

class TypeProduct(models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="type_p",
        verbose_name="Работа",
        default=0
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_t",
        verbose_name="Продукт",
    )

    class Meta:
        verbose_name = "Необходимый продукт для выполнения работы"
        verbose_name_plural = "Необходимые продукты для выполнения работы"
        constraints = [
            models.UniqueConstraint(
                fields=["type", "product"], name="uq_type_product"
            )
        ]
        ordering = ["type"]

class Order(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="order_type")
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_worker", blank=True, null=True, default=None)
    ready_product = models.ForeignKey(
        ReadyProduct,
        on_delete=models.CASCADE,
        verbose_name="Готовый продукт",
        related_name='order'
    )
    size = models.IntegerField(verbose_name="Размер")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_client")
    mail_index = models.CharField('Почтовый индекс', max_length=12)
    client_fullname = models.CharField('ФИО клиента', max_length=64)
    client_number = models.CharField('Номер клиента', max_length=24)
    date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True, null=True, blank=True)
    completed = models.BooleanField('Выполнено', default=False)

    @property
    def is_completed(self):
        return self.completed
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["id"]
