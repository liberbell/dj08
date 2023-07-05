from django.shortcuts import render

# Create your views here.
def index(request):
    val = "Good bye!"
    return render(request, "TemplateApp/index.html", context={"value": val})