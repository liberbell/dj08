import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())
# print(Students.objects.all()[:5])
# print(Students.objects.all()[5:])