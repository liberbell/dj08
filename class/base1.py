
class Car:
    couuntry = "Japan"
    year = 2019
    name = "Prius"

    def print_name(self):
        print("execute name print")
        print(self.name)

my_car = Car()
print(my_car.year)
my_car.print_name()

list_a = ["apple", "banana", Car]
second_car = list_a[2]()