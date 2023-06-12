
def outer():

    outer_value = "outer valuables"

    def inner():
        print("inner print")

    inner()
    print("outer value={}, id={}".format(outer_value, id(outer_value)))


outer()