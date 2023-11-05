from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Print user information"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name")
        parser.add_argument("age", type=int)
        parser.add_argument("--birthday", default="2023-01-01")
        parser.add_argument("three_words", nargs=3)
        parser.add_argument("--active", action="store_true")
        return super().add_arguments(parser)
    
    def handle(self, *args, **options):
        name = options["name"]
        age = options["age"]
        birthday = options["birthday"]
        three_words = options["three_words"]
        active = options["active"]
        print(active)
        print(type(age))
        print(f"name = {name}, age = {age}, birthday = {birthday}, Three words = {three_words}")