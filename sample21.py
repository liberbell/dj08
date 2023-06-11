import traceback

try:
    b = [10, 20, 30]
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    # print(e, type(e))
    traceback.print_exc()
    pass

except IndexError as e:
    print("index error")

except Exception as e:
    print("error", e)
print("end of calculation")