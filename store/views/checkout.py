from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from store.models.customer import Customer
from store.models.order import Order, OrderItem
from store.models.product import Product


def checkout_view(request):
    cart = request.session.get('cart')
    total_quantity = sum(cart.values())
    total = 0
    products_in_cart = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products_in_cart.append({
            'product': product,
            'quantity': quantity,
            'sub_total': product.price * quantity
        })
        total = total + product.price * quantity

    user = request.user

    context = {
        'products_in_cart': products_in_cart,
        'total_quantity': total_quantity,
        'total': total,
        'user': user,
    }
    print(context)
    return render(request, 'checkout.html', context)


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.user.id
        user = User.objects.get(id=customer_id)
        customer = Customer.objects.get(user=user)
        order = Order.objects.create(customer=customer, address=address, phone=phone)

        cart = request.session.get('cart')
        total = 0
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            price = product.price * quantity
            total = total + price

            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

        order.total_price = total
        order.save()

        request.session['cart'] = {}
        return redirect('store:order_list')
    return render(request, 'checkout.html')
