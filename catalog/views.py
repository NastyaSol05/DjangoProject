from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)
