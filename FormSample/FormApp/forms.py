from django import forms
from django.core import validators
from .models import Post, ModelSetPost, User

def check_name(value):
    if value == "abc":
        raise validators.ValidationError("Name Error")

class UserInfo(forms.Form):
    name = forms.CharField(label="Name", min_length=2, max_length=15, validators=[check_name])
    age = forms.IntegerField(label="Age", validators=[validators.MinValueValidator(20, message="Input over 20")])
    mail = forms.EmailField(
        label="E-mail",
        widget=forms.TextInput(attrs={"class": "mail_class", "placeholder": "sample@example.com"})
    )
    verify_mail = forms.EmailField(
        label="Verify E-mail",
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

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields["job"].widget.attrs["id"] = "id_job"
        self.fields["hobbies"].widget.attrs["class"] = "hobbies_class"

    def clean_homepage(self):
        homepage = self.cleaned_data["homepage"]
        if not homepage.startswith("https"):
            raise forms.ValidationError("Please enter https")
        
    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data["mail"]
        verify_mail = cleaned_data['verify_mail']
        if mail != verify_mail:
            raise forms.ValidationError("Unmatch email")
        
class BaseForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        print(f"Form: {self.__class__.__name__} done.")
        return super(BaseForm, self).save(*args, **kwargs)

class PostModelForm(BaseForm):
    name = forms.CharField(label="Name2")
    title = forms.CharField(label="Title2")
    memo = forms.CharField(max_length=255,
        label="Memo2",
        widget=forms.Textarea(attrs={"rows": 30, "cols": 20})
    )
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ["name", "title"]
        # exclude = ["title"]

    def save(self, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)
        obj.name = obj.name.upper()
        print(type(obj))
        print("Saved!")
        obj.save()
        return obj
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "abc":
            raise forms.ValidationError("cant register name")
        return name
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title == "test":
            raise forms.ValidationError("cant register title")
        return title
    
    def clean(self):
        clead_data = super().clean()
        title = clead_data.get("title")
        is_exists = Post.objects.filter(title=title).first()
        if is_exists:
            raise forms.ValidationError("The title is already registered")
        
class FormSetPost(forms.Form):
    title = forms.CharField(label="Title")
    memo = forms.CharField(label="Memo")

class ModelFormSetPost(forms.ModelForm):
    title = forms.CharField(label="Title")
    memo = forms.CharField(label="Memo")

    class Meta:
        model = ModelSetPost
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
