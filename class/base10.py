
class Human:
    
    __class_val = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age


human = Human("George", 61)
print(human.name)