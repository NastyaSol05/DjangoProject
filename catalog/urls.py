from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import products_detail, products_list
from config import settings

app_name = CatalogConfig.name


urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
