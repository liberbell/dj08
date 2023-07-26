import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())
# print(Students.objects.all()[:5])
# print(Students.objects.all()[5:])
# print(Students.objects.all()[5:8])

# print(Students.objects.filter(name="John").all())
# print(Students.objects.filter(age=17).all())

print(Students.objects.filter(name='John', pk=9).all())
print(Students.objects.filter(name="John", pk_gt=13).all())