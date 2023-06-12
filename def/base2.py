
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