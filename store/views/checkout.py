from django.shortcuts import render

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