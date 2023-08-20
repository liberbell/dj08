from .models import Students
from django import forms

class StudentInsertForm(forms.ModelForm):

    name = forms.CharField(label="Name: ")
    age = forms.IntegerField(label="Age: ")
    grade = forms.IntegerField(label="Grade: ")
    picture = forms.FileField(label="Picture: ")

    class Meta:
        model = Students
        fields = "__all__"

class StudentEditForm(forms.Form):
    name = forms.CharField(label="Name: ")
    age = forms.IntegerField(label="Age: ")
    grade = forms.IntegerField(label="Grade: ")
    picture = forms.FileField(label="Picture: ", required=False)

class StudentDeleteForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)