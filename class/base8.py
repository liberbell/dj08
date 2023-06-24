
class Meta1(type):

    def __new__(metacls, name, bases, class_dict):
        print("metacls = {}".format(metacls))
        print("name = {}".format(name))