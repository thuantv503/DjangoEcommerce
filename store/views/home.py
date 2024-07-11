import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

logger = logging.getLogger(__name__)


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        add = request.POST.get('add')
        cart = request.session.get('cart', {})
        if cart:
            quantity = cart.get(product)
            if quantity is not None:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                elif add:
                    if product in cart:
                        cart[product] = quantity + 1
                    else:
                        cart[product] = 1
            elif add:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart:', request.session['cart'])
        return redirect('store:store')

    def get(self, request):
        return HttpResponseRedirect(f'/{request.get_full_path()[1:]}index/')


def store(request):
    cart = request.session.get('cart')
    total_quantity = sum(cart.values())
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category=categoryID)
    else:
        products = Product.objects.all()

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['cart'] = cart
    data['quantity'] = total_quantity

    return render(request, 'index.html', data)
