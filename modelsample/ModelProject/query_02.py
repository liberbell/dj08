import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())

ids = [13, 14, 15]
print(Students.objects.filter(pk__in=ids).all())