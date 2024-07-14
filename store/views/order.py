from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from store.models.customer import Customer
from store.models.order import Order, OrderItem
from store.models.product import Product


def order_list_view(request):
    customer_id = request.user.id
    if customer_id:
        user = User.objects.get(id=customer_id)
        customer = Customer.objects.get(user=user)
        orders = Order.objects.filter(customer=customer)

        cart = request.session.get('cart')

        total_quantity = sum(cart.values())
        total = 0

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total = total + product.price * quantity

        context = {
            'orders': orders,
            'total_quantity': total_quantity,
            'total': total
        }

        return render(request, 'order-list.html', context)


def order_detail(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    context = {
        'order': order,
        'order_items': order_items,
    }
    html = render_to_string('order-detail.html', context)
    return JsonResponse({'html': html})
