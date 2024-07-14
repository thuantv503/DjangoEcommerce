from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from store.models.customer import Customer
from store.models.order import Order, OrderItem


def order_list_view(request):
    customer_id = request.user.id
    user = User.objects.get(id=customer_id)
    customer = Customer.objects.get(user=user)
    orders = Order.objects.filter(customer=customer)

    context = {
        'orders': orders,
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
