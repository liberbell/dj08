

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