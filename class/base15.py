
class WithTest:

    def __init__(self, file_name):
        print("init called")
        self.__file_name = file_name

    def __enter__(self):
        print("entr called")
        print(self.msg)

    def __exit__(self, exc_type, exc_val, traceback):
        print("exit called")

with WithTest("hello") as t:
    print("inside with")