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

def sample1(request):
    return render(request, "sample1.html")

def sample2(request):
    return render(request, "sample2.html")

def sample(request):
    name = "eric clapton"
    height = 181.4
    weight = 72.5
    bmi = weight / (height / 100)**2

    page_url = "HomePage: https://www.google.com"
    favorite_fruits = ["apple", "grape", "lemon"]
    msg = """Hello
    my name is eric"""
    msg2 = "0123456789"

    return render(request, "sample.html", context={
                  "name": name,
                  "height": height,
                  "weight": weight,
                  "page_url": page_url,
                  "favorite_fruits": favorite_fruits,
                  "bmi": bmi,
                  "msg": msg,
                  "msg2": msg2
    })