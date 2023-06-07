car = {"brand": "toyota", "model": "Prius", "year": 2015}

tmp_car = {"country": "Japan", "prefecture": "Aichi", "model": "Carola"}

car.update(tmp_car)
print(car)

car["city"] = "Toyota-shi"
car["year"] = 2017
print(car)

value = car.popitem()
print(car)
print(value)

value = car.pop("model")
print(car)
print(value)

car.clear()
print(car)

del car
print(car)