
class ClassA:
    def __init__(self, a):
        self.a = a

    def __bool__(self):
        if self.a == "A":
            return True
        else:
            return False

var = []
print("bool calculation:{}".format(bool(var)))
if var:
    print("inside if route")