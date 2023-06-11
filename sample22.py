
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divide by zero")
    else:
        return a / b
    
try:
    c = devide(10, 0)