from django.shortcuts import render
from django.forms import formset_factory
from . import forms

# Create your views here.
def index(request):
    return render(request, "formapp/index.html")

def form_page(request):
    form = forms.UserInfo()
    if request.method == "POST":
        form = forms.UserInfo(request.POST)
        if form.is_valid():
            print("validation successful")
            print(
                f"name: {form.cleaned_data['name']}, mail:{form.cleaned_data['mail']}, age:{form.cleaned_data['age']}"
            )
            print(form.cleaned_data)
    return render(request, "formapp/form_page.html", context={
        "form": form
    })

def form_post(request):
    form = forms.PostModelForm()
    if request.method == "POST":
        form = forms.PostModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "formapp/form_post.html", context={'form': form})

def form_set_post(request):
    TestFormset = formset_factory(forms.FormSetPost)
    formset = TestFormset()
    return render(request,
                  "formapp/formset_set_post.html",
                  context={"formset": formset}
    )