
class MyException(Exception):
    pass


def devide(a, b):
    if b == 0:
        # raise ZeroDivisionError("Divide by zero")
        raise MyException("Divide by zero")
    else:
        return a / b
    
try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))