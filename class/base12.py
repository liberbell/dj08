
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