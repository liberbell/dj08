
def generator(max):

    print("create Generator")
    for n in range(max):
        yield n
        print("yield!")

gen = generator(10)
# n = next(gen)
# print("n = {}".format(n))
# n = next(gen)
# print("n = {}".format(n))

for x in gen:
    print("x = {}".format(x))