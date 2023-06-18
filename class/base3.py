
class SampleClass():

    def __init__(self, msg, name=None):
        print("call the constructor")
        self.msg = msg
        self.name = name

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass("hello", "Eric")
