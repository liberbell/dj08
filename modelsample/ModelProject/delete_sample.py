import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Person
from django.utils import timezone

Person.objects.filter(first_name="Alex").delete()