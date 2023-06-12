
def print_animal():
    global animal
    animal="cat"
    print("inside def animal:{} id={}".format(animal, id(animal)))

animal = "Dog"

print_animal()
print("outside def animal:{} id={}".format(animal, id(animal)))