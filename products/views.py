from django.shortcuts import render


def products(request):
    return render(request, 'products/products.html')


def add_products(request):
    return render(request, 'products/add-products.html')


def update_products(request):
    return render(request, 'products/update-products.html')
