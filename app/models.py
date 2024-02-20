from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Product(models.Model):
    class CategoryChoices(models.TextChoices):
        Vegetables = 'овощи'
        Fruits = 'фрукты'
        Meat = 'мясо'
        Drinks = 'напитки'
        Others = 'другое'
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.CharField(max_length=7, choices=CategoryChoices.choices)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:150]
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list')

    def __str__(self):
        return self.title
