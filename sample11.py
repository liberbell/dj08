car = {"brand": "toyota", "model": "Prius", "year": 2015}

tmp_car = {"country": "Japan", "prefecture": "Aichi", "model": "Carola"}

car.update(tmp_car)
print(car)

car["city"] = "Toyota-shi"
car["year"] = 2017
print(car)