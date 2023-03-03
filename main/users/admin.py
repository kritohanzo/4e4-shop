from django.contrib import admin

from .models import Worker
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "name_surname", "number", "password")
    search_fields = ("name_surname",)
    list_editable = ("name_surname", "number", "password")
    empty_value_display = "-пусто-"

admin.site.register(Worker, WorkerAdmin)