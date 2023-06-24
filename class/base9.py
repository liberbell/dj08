
from abc import abstractmethod, ABCmeta

class Human(metaclass=ABCmeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_somthing(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    pass

human = Woman("alex")