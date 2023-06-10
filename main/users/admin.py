from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "confirmed", "worker")
    list_filter = ("username", "email")
    list_editable = ("username", "email", "confirmed", "worker")
    empty_value_display = "-пусто-"

admin.site.register(User, UserAdmin)
