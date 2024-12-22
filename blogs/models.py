from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок", help_text="Введите заголовок статьи: ")
    content = models.TextField(
        max_length=3000, null=True, verbose_name="Содержание", blank=True, help_text="Введите содержание статьи: "
    )
    image = models.ImageField(
        upload_to="blog/images",
        verbose_name="Фотография",
        blank=True,
        null=True,
        help_text="Загрузите фотографию статьи: ",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано", help_text="Опубликовать статью: ")
    views_counter = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров", help_text="Счетчик просмотров статьи: "
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
