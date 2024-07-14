from django.contrib import admin
from .models.product import Product
from .models.customer import Customer
from .models.order import Order, OrderItem
from .models.category import Category


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'address', 'phone', 'date', 'status')
    list_filter = ('status',)


# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(OrderItem)
