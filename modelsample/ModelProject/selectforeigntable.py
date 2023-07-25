import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Students, Schools, Prefectures

s = Schools.objects.first()
print(s)
print(dir(s))
print(s.prefecture.name)
st = s.students_set
print(type(st))
print(dir(st))