import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Person

p = Person(
    first_name = "Eric", last_name = "Clapton", birthday = "2000-01-01",
    email = "eric@example.com", salary =20000 , memo = "This is a memo",
    web_site = "https://www.google.com"
)

p = Person(
    first_name = "Eric", last_name = "Clapton", birthday = "2000-01-01",
    email = "eric@example.com", salary =None , memo = "This is a memo",
    web_site = "https://yahoo.com"
)
# p.save()

Person.objects.create(
    first_name = "Alex", last_name = "Hepp", email = "alex@example.com", salary = 1500, memo = "class method",
    web_site = None
)

obj, created = Person.objects.get_or_create(
    first_name = "George", last_name = "Harrison", email = "george@example.com", salary = 1500, memo = "class method",
    web_site = None
)
print(obj)
print(created)