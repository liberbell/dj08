

class Human:
    
    def __init__(self, name ,age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + "," + str(self.age) + "," + self.phone_number
    
man = Human("Alex", 32, "111-222-3333")
man_str = str(man)
print(man_str)