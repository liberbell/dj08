

class Human:
    
    def __init__(self, name ,age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + "," + str(self.age) + "," + self.phone_number
    
    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)
    
    def __hash__(self) -> int:
        return hash(self.name + self.phone_number)
    
    def __bool__(self):
        return True if self.age >- 20 else False
    
    
man = Human("Alex", 32, "111-222-3333")
man2 = Human("Alex", 18, "111-222-3333")
man3 = Human("Eric", 18, "111-222-4444")
man_str = str(man)
print(man_str)
print(man == man2)

set_men = {man, man2, man3}
for x in set_men:
    print(x)

if man:
    print("Man is true")
if man2:
    print("Man is false")