import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Students, Schools, Prefectures

# s = Schools.objects.first()
# print(s)
# print(dir(s))
# print(s.prefecture.name)
# st = s.students_set
# print(type(st))
# print(dir(st))

# print(st.all())
# print(s.students_set.all())

from ModelApp.models import Places, Restaurants

# p = Places.objects.first()
# print(type(p), print(dir(p)))
# print(p.restaurants.name)
# r = Restaurants.objects.first()
# print(r.place.name)

from ModelApp.models import Books, Authors

b = Books.objects.first()
print(b.authors.all())
r = Authors.objects.first()
print(r.books_set.all())