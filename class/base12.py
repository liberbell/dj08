
class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        print("call getter name")
        return self.__name
    
    @property
    def age(self):
        print("call getter age")
        return self.__age
    
    @name.setter
    def name(self, name):
        print("call setter name")
        self.__name = name

    @age.setter
    def age(self, age):
        print("call setter age")
        if age < 0:
            print("set up to zero")
            return
        self.__age = age