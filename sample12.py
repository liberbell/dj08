fruit = ("apple", "banana", "lemon")
print(fruit)
print(fruit[0])
print(type(fruit))

# fruit[1] = "orange"

fruit = fruit + ("orange",)
print(fruit)

list_fruit = ["apple", "banana"]
fruit = tuple(list_fruit)
print(fruit)
print(type(fruit))

print(fruit.count("apple"))
print(fruit.index("banana"))