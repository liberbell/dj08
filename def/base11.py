
list_a = (1, 2, 3, "a", 5, "b")
list_b = [x * 2 for x in list_a if type(x) == int]
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)

dict_a = {
    "a": "Apple",
    "b": "Banana",
}

list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c)