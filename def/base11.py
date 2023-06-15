
list_a = (1, 2, 3, "a", 5, "b")
list_b = [x * 2 for x in list_a if type(x) == int]
print(list_b)