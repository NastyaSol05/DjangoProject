from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название категории", help_text="Введите название категории: "
    )
    description = models.TextField(null=True, verbose_name="Описание", blank=True, help_text="Введите описание:")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта", help_text="Введите название продукта: ")
    description = models.TextField(null=True, verbose_name="Описание", blank=True, help_text="Введите описание: ")
    image = models.ImageField(
        upload_to="products/images",
        verbose_name="Фотография",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта: ",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="Категория", help_text="Укажите категорию: "
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Введите цену: ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
