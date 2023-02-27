import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            old_phone = Phone.objects.filter(id=phone['id'])
            if not old_phone:
                new_phone = Phone(
                    id=phone['id'],
                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=phone['name'].lower().replace(' ', '-')
                )
                new_phone.save()
            else:
                print(f"Error: ID phone: {phone['id']}, exists in DB")
