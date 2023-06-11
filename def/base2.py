
def sample(arg1, arg2=100):
    print(arg1, arg2)

sample(200, 300)
sample(150)

def spam(arg1, *arg2):
    print("arg1 len:", len(arg1))
    print("arg2 len:", len(arg2))