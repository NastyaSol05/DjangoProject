from django.contrib import admin

from blogs.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at")
    list_filter = ("is_published",)
    search_fields = (
        "title",
        "content",
    )
