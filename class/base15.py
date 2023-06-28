
class WithTest:

    def __init__(self):
        print("init called")

    def __enter__(self):
        print("entr called")

    def __exit__(self, exc_type, exc_val, traceback):
        print("exit called")