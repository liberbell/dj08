# list_a = [1, 2, 3, 4]
# list_b = []

# print(list_a, list_b)
# print(list_a[0], list_b)

# list_a = [1, [1, 2, "apple"], 3, "banana"]
# print(list_a[1][2])

# list_a[1][2] = "lemon"
# print(list_a)
# list_a.reverse()
# print(list_a)

list_a = [1, 2, 3, 4, 5]
list_b = list_a[1:4:2]
print(list_b)

list_a.append("apple")
print(list_a)

list_a.extend(["banana", "lemon"])
print(list_a)

list_a.insert(1, "grage")
print(list_a)

# list_a.clear()
# print(list_a)

list_a = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
print(list_a)
list_a.remove(3)
print(list_a)