
class WithTest:

    def __init__(self):
        print("init called")

    def __enter__(self):
        print("entr called")