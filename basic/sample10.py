car = {"brand": "toyota", "model": "Prius", "year": 2015, 1:100}
# print(car["brand"])

print(car.get("bran", "does not exist"))
print(car.get(1))
print(car.keys())
print(car.values())
print(car.items())

for k, v in car.items():
    print("key is:", k)
    print("value is:", v)

if "brand" in car:
    print("brand is", car["brand"])