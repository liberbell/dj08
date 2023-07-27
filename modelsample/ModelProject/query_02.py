import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students, Person

# print(Students.objects.all())

ids = [13, 14, 15]
# print(Students.objects.filter(pk__in=ids).all())

# print(Students.objects.filter(name__contains="h").all())

p = Person(
    first_name = "Alex", last_name = "Hepp", birthday = "2000-01-01",
    email = "alex@example.com", salary =100 , memo = "This is a memo",
    web_site = "https://www.google.com"
)
p.save()