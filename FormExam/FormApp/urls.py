from django.urls import path
from . import views

app_name = "form_app"

urlpatterns = [
    path("insert_student/", views.insert_student, name="insert_student"),
    path("students_list/", views.students_list, name="students_list"),
    path("edit_student/<key:id>", views.edit_student, name="edit_student"),
]
