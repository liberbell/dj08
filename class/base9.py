
from abc import abstractmethod as ABCmeta

class Human(metaclass=ABCmeta):

    def __init__(self, name):
        self.name = name