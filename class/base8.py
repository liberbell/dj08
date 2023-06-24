
class Meta1(type):

    def __new__(metacls, name, bases, class_dict):
        print("metacls = {}".format(metacls))
        print("name = {}".format(name))
        print("bases = {}".format(bases))
        print("class_dict = {}".format(class_dict))

        return super().__new__(metacls, name, bases, class_dict)