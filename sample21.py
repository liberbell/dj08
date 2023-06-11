
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(e, type(e))
    pass
print("end of calculation")