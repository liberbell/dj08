import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students, Schools

# for student in Students.objects.all():
#     print(student.name, student.school.name, student.school.prefecture.name)

# for student in Students.objects.filter(school__name="West high school").all():
#     print(student.name, student.school.name, student.school.prefecture.name)

for student in Students.objects.exclude(school__name="West high school").all():
    print(student.name, student.school.name, student.school.prefecture.name)