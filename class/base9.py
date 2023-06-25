
from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_somthing(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    
    def say_something(self):
        print("Woman: name={}".format(self.name))

class Man(Human):
    
    def say_something(self):
        print("Man: name={}".format(self.name))

human = Woman("alex")