
from abc import abstractmethod as ABCmeta

class Human(metaclass=ABCmeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_somthing(self):
        pass

    def say_name(self):
        print(self.name)