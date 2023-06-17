
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 100)
        func(*args, **kwargs)
        print("*" * 100)
    return wrapper

@my_decorator
