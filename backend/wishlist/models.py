from django.db import models
from django.utils import timezone


class Wish(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    achieved = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)
    added_at = models.DateTimeField(default=timezone.now)
    reserved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
