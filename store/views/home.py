from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self, request):
        context = {
            'variable': 'value',  # Dữ liệu context bạn muốn truyền vào template
        }
        return render(request, 'index.html', context)
