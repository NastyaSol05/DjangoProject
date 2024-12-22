from django.conf.urls.static import static
from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView
from config import settings

app_name = BlogsConfig.name


urlpatterns = [
    path("", ArticleListView.as_view(), name="articles_list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="articles_detail"),
    path("articles/create", ArticleCreateView.as_view(), name="articles_create"),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="articles_update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="articles_delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
