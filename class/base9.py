
from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    
    def say_something(self):
        print("Woman: name={}".format(self.name))

class Man(Human):
    
    def say_something(self):
        print("Man: name={}".format(self.name))

num = input("input 1 or 0:")
if num == "0":
    human = Man("Eric")
elif num == "1":
    human = Woman("Alex")
else:
    print("Invalid input")

human.say_something()