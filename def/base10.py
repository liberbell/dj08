
def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a - 1)

sample(10)

def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)

for x in range(10):
    print(fib(x))