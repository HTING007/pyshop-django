from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fruit', 'Fruit'),
        ('drink', 'Drink'),
        ('snack', 'Snack'),
    ]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code

