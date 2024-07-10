from django.db import models
from .product import Product
from .customer import Customer
from datetime import datetime


class Order(models.Model):
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

