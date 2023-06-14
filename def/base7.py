
def sub_sub_generator():
    yield "sub sub generator"
    return "sub sub return"

def sub_generator():
    yield "sub generator"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "sub return"

def generator():
    yield "generator"
    res = yield from sub_generator()
    print("res = {}".format(res))

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))