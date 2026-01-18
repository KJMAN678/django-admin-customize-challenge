from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from web.models import Author, Book


class Command(BaseCommand):
    help = "Make dummy data"

    def handle(self, *args, **options):
        fake = Faker("ja_JP")
        for _ in range(10):
            author = Author.objects.create(name=fake.name(), email=fake.email())
            Book.objects.create(title=fake.sentence(), author=author)
        self.stdout.write(
            self.style.SUCCESS("10件のAuthorとBookのダミーデータを作成しました")
        )
