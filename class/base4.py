
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