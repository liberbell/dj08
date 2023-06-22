
class ClassA:
    def __init__(sel, name):
        self.a_name = name

    def print_a(self):
        print("execute ClassA method")
        print("a = {}".format(self.a_name))

    def print(self):
        print("A hi")

class ClassB:
    def __init__(self, name):
        self.b_name = name

    def print_b(self):
        print("execute ClassB method")
        print("b = {}".format(self.b_name))

    def print(self):
        print("B hi")

class NewClass(ClassA, ClassB):
    def __init__(self, a_name, b_name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)