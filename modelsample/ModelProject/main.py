import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Person

p = Person(
    first_name = "Eric", last_name = "Clapton", birthday = "2000-01-01",
    email = "eric@example.com", salary = "20000", momo = "This is a memo",
    web_site = "https://www.google.com"
)
p.save()