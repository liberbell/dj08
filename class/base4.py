
class Human:

    class_name = "Human"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print("execute instance method")
        print("name: {}, age: {}".format(self.name, self.age))