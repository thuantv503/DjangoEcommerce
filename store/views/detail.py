from django.shortcuts import render, get_object_or_404

from store.models.product import Product


def product_detail(request):
    id = request.GET.get('product_id')
    detail_product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    total_quantity = sum(cart.values())
    product_quantity = cart.get(id, 0)

    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity


    context = {}
    context['product'] = detail_product
    context['total_quantity'] = total_quantity
    context['total'] = total
    context['cart'] = cart
    context['product_quantity'] = product_quantity

    return render(request, 'shop-details.html', context)
