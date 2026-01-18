from django.core.management.base import BaseCommand

from web.models import Author, Book


class Command(BaseCommand):
    help = "Query dummy data"

    def handle(self, *args, **options):
        book = Book.objects.select_related("author").get(id=1)
        self.stdout.write(
            self.style.SUCCESS(f"Book: {book.title}, Author: {book.author.name}")
        )
