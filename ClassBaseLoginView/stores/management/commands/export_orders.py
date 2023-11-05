from django.core.management.base import BaseCommand
from stores.models import Orders

class Command(BaseCommand):

    def handle(self, *args, **options):

        return super().handle(*args, **options)