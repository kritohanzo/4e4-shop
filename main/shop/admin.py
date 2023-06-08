from django.contrib import admin

from .models import ReadyProduct


class ReadyProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "selling_price_per_unit", "available_quantity", "picture", "model")
    search_fields = ("name",)
    list_filter = ("id",)
    list_editable = ("name", "selling_price_per_unit", "picture", "model")
    empty_value_display = "-пусто-"


admin.site.register(ReadyProduct, ReadyProductAdmin)
