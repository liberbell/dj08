import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

from django import setup
setup()
from ModelApp.models import Restaurants, Places

places = [("Palo Alto", "San Francisco"), ("Sodo", "Seattle")]
restaurants = ["restaurant A", "restaurant B"]

for place_name, place_address in places:
    p = Places(name=place_name, address=place_address)
    p.save()
    for restaurant_name in restaurants:
        # r = Restaurants(place=p, name=restaurant_name)
        # r.save()
        Restaurants.objects.create(
            place=p, name=restaurant_name
        )