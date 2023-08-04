from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age")
    mail = forms.EmailField(label="E-mail", widget=forms.TextInput)
    is_married = forms.BooleanField(label="Married")
    birthday = forms.DateField()
    salary = forms.IntegerField()
    job = forms.ChoiceField(choices=(
        (1, "Permanent"),
        (2, "Temporary"),
        (3, "Student"),
        (4, "No job")
    ))
    hobbies = forms.MultipleChoiceField(choices=(
        (1, "Baseball"),
        (2, "Books"),
        (3, "Movies"),
        (4, "Other")
    ))
    homepage = forms.URLField(required=False)
