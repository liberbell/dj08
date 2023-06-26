

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("call getter name")
        return self.__name

    def get_age(self):
        print("call getter age")
        return self.__age
    
    def set_name(self, name):
        print("call setter name")
        self.__name = name

    def set_age(self, age):
        print("call setter age")
        self.__age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)

human = Human("Eric", 67)
human.name = "Bob"
