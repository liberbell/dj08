from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("name")
        parser.add_argument("age")
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        name = options["name"]
        age = options["age"]