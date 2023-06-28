
class WithTest:

    def __init__(self, msg):
        print("init called")
        self.msg = msg

    def __enter__(self):
        print("entr called")
        print(self.msg)

    def __exit__(self, exc_type, exc_val, traceback):
        print("exit called")

with WithTest("hello") as t:
    print("inside with")