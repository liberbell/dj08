from django.shortcuts import render

# Create your views here.
def index(request):
    val = "Good bye!"
    return render(request, "TemplateApp/index.html", context={"value": val})

def home(request, first_name, last_name):
    my_name = f"{first_name} {last_name}"
    favorite_fruits = ["apple", "lemon", "grape"]
    my_info = {
        "name": "Eric",
        "age":  70
    }
    status = 20
    return render(request, "home.html", context={
        "my_name": my_name,
        "favorite_fruits": favorite_fruits,
        "my_info": my_info,
        "status": status
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
                  "fruits": favorite_fruits,
                  "bmi": bmi,
                  "msg": msg,
                  "msg2": msg2
    })

class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def sample3(request):
        country = Country("Japan", 100000000, "Tokyo")
        return render(request, "sample3.html", context={
            "country": country
        })