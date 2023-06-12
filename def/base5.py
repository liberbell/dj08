
def generator(max):

    print("create Generator")
    for n in range(max):
        yield n
        print("yield!")

gen = generator(10)