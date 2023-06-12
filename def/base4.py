
def outer():

    outer_value = "outer valuables"

    def inner():
        outer_value = "inner outer valuables"
        print("inner outer value={}, id={}".format(outer_value, id(outer_value)))
        print("inner print")

    inner()
    print("outer value={}, id={}".format(outer_value, id(outer_value)))


outer()