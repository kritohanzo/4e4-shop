from django.db import models
from users.models import Worker


class Work(models.Model):
    name = models.CharField("Наименование работы", max_length=64)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
        ordering = ["id"]


class Provider(models.Model):
    name = models.CharField("Наименование поставщика", max_length=64)
    number = models.CharField("Номер телефона", max_length=16)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["id"]


class Product(models.Model):
    name = models.CharField("Наименование продукта", max_length=64)
    purchase_price_per_unit = models.IntegerField("Цена закупки за штуку")
    available_quantity = models.IntegerField("Количество на складе")
    provider_id = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Поставщик",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["id"]

class WorkInProcess(models.Model):
    name = models.CharField("Наименование продукта", max_length=64)
    work_id = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="works_in_process")
    ready_product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="works_in_process")
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="works_in_process")

    class Meta:
        verbose_name = "Работа в процессе"
        verbose_name_plural = "Работы в процессе"
        ordering = ["id"]

class WorkProduct(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_p",
        verbose_name="Работа",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Продукт",
    )

    class Meta:
        verbose_name = "Необходимый продукт для выполнения работы"
        verbose_name_plural = "Необходимые продукт для выполнения работы"
        constraints = [
            models.UniqueConstraint(
                fields=["work", "product"], name="uq_work_product"
            )
        ]

class WorkWorker(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name="work_w",
        verbose_name="Работа",
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="worker",
        verbose_name="Работник",
    )

    class Meta:
        verbose_name = "Умение работника в определённой работе"
        verbose_name_plural = "Умения работников в определённой работе"
        constraints = [
            models.UniqueConstraint(
                fields=["work", "worker"], name="uq_work_worker"
            )
        ]
