import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, Classes

student = Students.objects.get(pk=101)
for test_result in student.testresults_set.all():
    print(student.class_fk.name, student.name, test_result.test.name, test_result.score)

from django.db.models import Sum, Avg, Max, Min

for class_summary in Classes.objects.values("name", "students__testresults__name").annotate(
    max_score = Max("students__testresults__score"),
    max_score = Max("students__testresults__score"),
    max_score = Max("students__testresults__score"),
    max_score = Max("students__testresults__score"), 
)