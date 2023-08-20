from django.shortcuts import render
from . import forms
from .models import Students
from django.core.files.storage import FileSystemStorage
import _osx_support

# Create your views here.
def insert_student(request):
    insert_form = forms.StudentInsertForm(request.POST or None, request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
        insert_form = forms.StudentInsertForm()
    return render(request, "formapp/insert_student.html",
                  context={'insert_form': insert_form})

def students_list(request):
    students = Students.objects.all()
    return render(
        request, "formapp/students_list.html",
        context={"students": students},
    )

def edit_student(request, id):
    student = Students.objects.get(id=id)
    update_form = forms.StudentEditForm(
        initial={
            "name": student.name,
            "age": student.age,
            "grade": student.grade,
            "picture": student.picture
        }
    )
    if request.method == "POST":
        update_form = forms.StudentEditForm(request.POST or None, request.FILES or None)
        if update_form.is_valid():
            student.name = update_form.cleaned_data["name"]
            student.age = update_form.cleaned_data["age"]
            student.grade = update_form.cleaned_data["grade"]
            picture = update_form.cleaned_data["picture"]
            if picture:
                fs = FileSystemStorage()
                file_name = fs.save(os.path.join("student", picture.name), picture)
                student.picture = file_name
            student.save()

    return render(request, "formapp/edit_student.html",
                  context={'update_form': update_form,
                           'student': student})