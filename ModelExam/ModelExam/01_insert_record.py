import os

os.environ.setdefault("django_SETINGS_MODLE", "ModelExam.settings")
from django import setup
setup()

from ModelApp.models import Students, TestResults, Tests, Classes
from random import randint

class_name = ["Class" + c for c in "ABCDEFGHIJ"]