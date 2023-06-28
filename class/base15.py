
class WithTest:

    def __init__(self, file_name):
        print("init called")
        self.__file_name = file_name

    def __enter__(self):
        print("entr called")
        print(self.msg)
        self.__file = open("self.__file_name", mode="w", encoding="utf-8")
        return self
    
    def write(self, msg):
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, traceback):
        print("exit called")
        self.__file.close()

with WithTest("hello") as t:
    print("inside with")