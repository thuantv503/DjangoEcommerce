from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def post(self, request):
        product = request.POST('product')
        remove = request.POST('remove')
        cart = request.POST('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')

    def get(self, request):
            context = {
                'variable': 'value',  # Dữ liệu context bạn muốn truyền vào template
            }
            return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
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

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)
