
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(args[0])
        if args[0] == 1:
            return 1
        print("*" * 100)
        func(*args, **kwargs)
        print("*" * 100)
    return wrapper

@my_decorator
def func_a(*args, **kwargs):
    print("execute func_a")
    print(args)

@my_decorator
def func_b(*args, **kwargs):
    print("execute func_b")
    print(args)

func_a(1, 2, 3)
func_b(2, 2, 3)