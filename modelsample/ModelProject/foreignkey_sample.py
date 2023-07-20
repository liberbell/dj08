import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Students, Schools, Prefectures

prefectures = ["Alaska", "Idaho"]
schools = ["West high school", "East high school", "South high school", "North high school"]
students = ["Eric", "Alex", "John"]

def insert_record():
    for prefecture_name in prefectures:
        prefecture = Prefectures(
            name = prefecture_name
        )