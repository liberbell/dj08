from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):

    name = forms.CharField(label="Name: ")
    age = forms.IntegerField(label="Age: ")
    grade = forms.IntegerField(label="Grade: ")
    picture = forms.FileField(label="Picture: ")