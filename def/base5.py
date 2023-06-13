
def generator(max):

    print("create Generator")
    for n in range(max):
        x = yield n
        print("x = {}".format(x))
        print("yield!")

gen = generator(10)
# n = next(gen)
# print("n = {}".format(n))
# n = next(gen)
# print("n = {}".format(n))

# for x in gen:
#     print("x = {}".format(x))

next(gen)
gen.send(100)