from django.contrib import admin
from .models.product import Product
from .models.customer import Customer
from .models.order import Order
from .models.category import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)

