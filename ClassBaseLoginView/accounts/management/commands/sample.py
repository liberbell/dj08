from django.core.management.base import BaseCommand


class BaseCommand(BaseCommand):
    
    def handle(self, *args, **options):
        print("Batch 1")