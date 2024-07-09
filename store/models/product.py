from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

