from django.contrib import admin
from .models import Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'link', 'price', 'achieved', 'reserved', 'added_at', 'reserved_at')