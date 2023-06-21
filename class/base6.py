
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello {}".format(self.name))

    def say_age(self):
        print("{} years old.".format(self.age))