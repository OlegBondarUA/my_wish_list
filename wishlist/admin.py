from django.contrib import admin
from .models import Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'link', 'price')