from django.shortcuts import render

# Create your views here.

class Member:

    def __init__(self, name, id, join_at, picture_path):
        self.name = name
        self.id = id
        self.join_at = join_at
        self.picture_path = picture_path


def home(request):
    return render(request, "home.html")

def members(request):
    pass