from django import forms

class UserInfo(forms.Form):
    name = forms.CharField(label="Name", min_length=2, max_length=15)
    age = forms.IntegerField(label="Age")
    mail = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={"class": "mail_class", "placeholder": "sample@example.com"})
    )
    is_married = forms.BooleanField(label="Married", initial=True)
    birthday = forms.DateField(initial="1900-01-01")
    salary = forms.IntegerField()
    job = forms.ChoiceField(choices=(
        (1, "Permanent"),
        (2, "Temporary"),
        (3, "Student"),
        (4, "No job")
    ), widget=forms.RadioSelect)
    hobbies = forms.MultipleChoiceField(choices=(
        (1, "Baseball"),
        (2, "Books"),
        (3, "Movies"),
        (4, "Other")
    ), widget=forms.CheckboxSelectMultiple)
    homepage = forms.URLField(required=False)
    memo = forms.CharField(label="Memo", widget=forms.Textarea)
