
def outer():

    outer_value = "outer valuables"

    def inner():
        print("inner print")

    inner()
    print(outer_value)


outer()