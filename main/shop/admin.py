from django.contrib import admin

from .models import ReadyProduct, Size, Type


class ReadyProductAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "model", "collection", "description", "selling_price_per_unit", "available_quantity", "color", "picture",)
    search_fields = ("type",)
    list_filter = ("id",)
    list_editable = ("type", "model", "collection", "description", "selling_price_per_unit", "picture",)
    empty_value_display = "-пусто-"

class ReadyProductSizeAdmin(admin.ModelAdmin):
    list_display = ("id", "size",)
    list_filter = ("size",)
    list_editable = ("size",)
    empty_value_display = "-пусто-"

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_filter = ("name",)
    list_editable = ("name",)
    empty_value_display = "-пусто-"

admin.site.register(ReadyProduct, ReadyProductAdmin)
admin.site.register(Size, ReadyProductSizeAdmin)
admin.site.register(Type, TypeAdmin)
