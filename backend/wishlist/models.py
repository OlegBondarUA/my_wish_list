from django.db import models


def wish_image_path(instance, filename):
    return f'images/{filename}'


class Wish(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=wish_image_path)
    link = models.URLField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    achieved = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
