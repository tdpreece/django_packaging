from django.core.management.base import BaseCommand

from ...models import Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        for person in Person.objects.all():
            person.age += 1
            person.save()
