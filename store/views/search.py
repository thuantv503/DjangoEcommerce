from django.shortcuts import render

from store.models.category import Category
from store.models.product import Product


def search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()

    total = 0
    total_quantity = 0
    categories = Category.objects.all()

    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    else:
        total_quantity = sum(cart.values())
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total += product.price * quantity

    context = {
        'query': query,
        'products': products,
        'total': total,
        'quantity': total_quantity,
        'categories': categories
    }
    return render(request, 'index.html', context)
