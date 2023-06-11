import traceback

try:
    a = 10 / 0
except ZeroDivisionError as e:
    # print(e, type(e))
    traceback.print_exc()
    pass
print("end of calculation")