import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Person

persons = Person.objects.all()

for person in persons:
    print(person.id, person, person.salary)

# person = Person.objects.get(first_name="Eric")
# person = Person.objects.get(pk=1)
# print(person.id, person)

persons = Person.objects.filter(first_name="Eric").all()
print(persons.id, persons)