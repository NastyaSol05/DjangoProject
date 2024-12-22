from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogs.urls", namespace="blogs")),
] + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
