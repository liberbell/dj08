from django.shortcuts import render
from . import forms
from .models import Students
from django.core.files.storage import FileSystemStorage

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
    edit_form = forms.StudentEditForm(
        initial={
            "name": student.name,
            "age": student.age,
            "grade": student.grade,
            "picture": student.picture
        }
    )
    if request.method == "POST":
        edit_form = forms.StudentEditForm(request.POST or None, request.FILES or None)
        if edit_form.is_valid():
            student.name = edit_form.cleaned_data["name"]
            student.age = edit_form.cleaned_data["age"]
            student.grade = edit_form.cleaned_data["grade"]
            picture = edit_form.cleaned_data["picture"]
            if picture:
                fs = FileSys

            student.save()

    return render(request, "formapp/edit_student.html",
                  context={'eidt_form': edit_form,
                           'student': student})