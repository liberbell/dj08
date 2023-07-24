import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Books, Authors

def insert_books():
    book1 = Books(name="now and then")
    book2 = Books(name="still danger")
    book3 = Books(name="yesterday")

    book1.save()
    book2.save()
    book3.save()

def insert_authors():
    author1 = Authors(name="Mark")
    author2 = Authors(name="Earnest")
    author3 = Authors(name="Edgar")

    author1.save()
    author2.save()
    author3.save()