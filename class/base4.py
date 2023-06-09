
class Human:

    class_name = "Human"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print("execute instance method")
        print("name: {}, age: {}".format(self.name, self.age))

    @classmethod
    def print_class_name(cls, msg):
        print("execute class method")
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg):
        print("execute static method")
        print(msg)

Human.print_class_name("Hello")
man = Human("Eric", 65)
man.print_name_age()
man.print_msg("Hello static")
Human.print_msg("Hello static")