from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")