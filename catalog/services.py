from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set("product_list", product)
    return product


class ProductService:

    @staticmethod
    def get_product_by_category(category):
        return Product.objects.filter(category=category)
