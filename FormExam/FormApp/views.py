from django.shortcuts import render
from . import forms
from .models import Students

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