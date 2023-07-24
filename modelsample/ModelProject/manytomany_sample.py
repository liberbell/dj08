import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Books, Authors

def insert_books():
    book1 = Books(name="now and then")
    book2 = Books(name="still danger")