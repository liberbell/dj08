car = {"brand": "toyota", "model": "Prius", "year": 2015, 1:100}
# print(car["brand"])

print(car.get("bran", "does not exist"))
print(car.get(1))
print(car.keys())
print(car.values())
print(car.items())