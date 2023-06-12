
def outer():

    def inner():
        print("inner print")

    inner()


outer()