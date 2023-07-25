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

# insert_books()
# insert_authors()

book1 = Books.objects.get(pk=1)
author1 = Authors.objects.get(pk=1)
author2 = Authors.objects.get(pk=2)
# book1.authors.add(author1, author2)

print(book1.authors.all)