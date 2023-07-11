from django.shortcuts import render

# Create your views here.

class Member:

    def __init__(self, id, name, join_at, picture_path):
        self.name = name
        self.id = id
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Member(0, "Eric", "2023/01/10", "image/eric.jpg"),
    Member(1, "Bob", "2023/01/20", "image/bob.jpg"),
    Member(2, "Alex", "2023/01/05", "image/alex.jpg"),
    Member(3, "Elton", "2023/02/04", "image/elton.jpg")
]


def home(request):
    return render(request, "home.html")

def members(request):
    pass