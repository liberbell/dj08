
def outer():

    outer_value = "outer valuables"

    def inner():
        nonlocal outer_value
        outer_value = "inner outer valuables"
        print("inner outer value={}, id={}".format(outer_value, id(outer_value)))

    inner()
    print("outer value={}, id={}".format(outer_value, id(outer_value)))


outer()