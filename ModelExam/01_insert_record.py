import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes
from random import randint

class_names = ["Class" + c for c in "ABCDEFGHIJ"]
student_names = ["Student" + c for c in "ABCDEFGHIJ"]
test_names = ["math", "grammer", "science"]

# print(class_name)

inserted_tests = []
for test_name in test_names:
    test = Tests(name=test_name)
    test.save()
    inserted_tests.append(test)

for class_name in class_names:
    insert_class = Classes(name=class_name)
    insert_class.save()