from django.core.management import call_command
from django.core.management.base import BaseCommand

from blogs.models import Article


class Command(BaseCommand):
    help = "Add test articles to the database"

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All existing articles have been deleted."))

        articles = [
            {
                "title": "Пишем статью о карточках",
                "content": "Использование карточек для создания привычных и эффективных решений.",
                "published_at": "2021-01-01",
            },
            {
                "title": "Как писать качественный текст",
                "content": "Наилучший текст состоит из коротких абзацев и понятных слов.",
                "published_at": "2021-02-01",
            },
        ]

        for article_data in articles:
            article, created = Article.objects.get_or_create(**article_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added article: {article.title}"))
                call_command("loaddata", "blogs.json")
                self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))

            else:
                self.stdout.write(self.style.WARNING(f"Article already exists: {article.title}"))
