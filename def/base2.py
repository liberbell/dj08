
def sample(arg1, arg2=100):
    print(arg1, arg2)

sample(200, 300)
sample(150)

def spam(arg1, *arg2):
    print("arg1 len:", arg1)
    print("arg2 len:", arg2)
    print(type(arg2))

spam(1, 2, 3, 4, 5)

def spam2(arg1, **arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))
    print(type(arg2))

spam2(3, name="Bob", age=20)

def spam3(arg1, *arg2, **arg3):
    print("arg1: {}, arg2: {}, arg3: {}".format(arg1, arg2, arg3))

spam3(1, 2, 3, 4, 5, name="Bob", age=23)

def sample2():
    return 1, 2

a, b = sample2()
print(a, b)