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
            name=prefecture_name
        )
        prefecture.save()

        for school_name in schools:
            school = Schools(
                name=school_name,
                prefecture=prefecture
            )
            school.save()

            for student_name in students:
                student=Students(
                    name=student_name,
                    age=17,
                    major="Pysics",
                    school=school,
                    prefecture=prefecture
                )
                student.save()



def select_students():
    students=Students.objects.all()
    for student in students:
        print(student.id, student.name, student.school.id, student.school.name, student.school.prefecture.id, student.school.prefecture.name)

insert_record()
select_students()

# Schools.objects.filter(id=1).delete()

# Prefectures.objects.filter(id=1).delete()