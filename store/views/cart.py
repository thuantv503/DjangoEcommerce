from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from store.models.product import Product


def cart(request):
    cart = request.session.get('cart', {})
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
    return render(request, 'shoping-cart.html', context)


@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id, None)

        request.session['cart'] = cart

        total_quantity = sum(cart.values())
        total = 0
        product = Product.objects.get(id=product_id)
        price = product.price
        for id, qty in cart.items():
            product = Product.objects.get(id=id)
            total += product.price * qty

        return JsonResponse({'total_quantity': total_quantity, 'total': total,
                             'product_id': product_id, 'quantity': quantity, 'price': price})

