import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.count())
# print(Students.objects.filter(name="John").count())

from django.db.models import Count, Max, Avg, Min, Sum

# print(Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age')))
# aggregate_student = Students.objects.aggregate(Count('pk'), Max('pk'), Min('pk'), Avg('pk'), Sum('age'))

# print(aggregate_student["pk__avg"])

print(Students.objects.values("name").annotate(
    Max("pk"), Min("pk")
))