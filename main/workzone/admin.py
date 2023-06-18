from django.contrib import admin

from .models import Provider, Product, TypeProduct, Order


class ProviderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "number",)
    search_fields = ("name",)
    list_filter = ("id",)
    list_editable = ("name", "number",)
    empty_value_display = "-пусто-"

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "purchase_price_per_unit", "available_quantity", "provider",)
    list_filter = ("name",)
    list_editable = ("name", "available_quantity",)
    empty_value_display = "-пусто-"

class TypeProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "type",)
    empty_value_display = "-пусто-"

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "ready_product_id", "type_id", "client_fullname", "client_number", "mail_index", "size", "date", "worker_id", "completed")
    list_filter = ("client_fullname", "client_number", "worker_id",)
    list_editable = ("client_fullname", "client_number", "mail_index",)
    empty_value_display = "<нет>"

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(Order, OrderAdmin)
