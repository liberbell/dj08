from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("--birthday")
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        name = options["name"]
        age = options["age"]
        birthday = options["birthday"]
        print(f"name = {name}, age = {age}", birthday = {birthday})