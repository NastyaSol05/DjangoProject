from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All existing products have been deleted.'))

        category1, _ = Category.objects.get_or_create(name='Овощи')

        products = [
            {'name': 'Помидор', 'description': 'Спелый, сочный и красный', 'category': category1, 'price': 11},
            {'name': 'Огурец', 'description': 'Свежий и сочный', 'category': category1, 'price': 23},
        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))