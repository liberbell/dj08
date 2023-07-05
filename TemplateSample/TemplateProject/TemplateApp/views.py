from django.shortcuts import render

# Create your views here.
def index(request):
    val = "Good bye!"
    return render(request, "TemplateApp/index.html", context={"value": val})

def home(request):
    my_name = "Eric"
    favorite_fruits = ["apple", "lemon", "grape"]
    my_info = {
        "name": "Eric",
        "age":  70
    }
    return render(request, "home.html", context={
        "my_name": my_name,
        "favorite_fruits": favorite_fruits,
        "my_info": my_info
    })