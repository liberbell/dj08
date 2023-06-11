import traceback

try:
    b = [10, 20, 30]
    c = b.method()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    # print(e, type(e))
    traceback.print_exc()
    pass

except IndexError as e:
    print("index error")

except Exception as e:
    print("error", type(e))
print("end of calculation")