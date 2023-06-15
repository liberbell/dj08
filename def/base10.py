
def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a - 1)

sample(10)