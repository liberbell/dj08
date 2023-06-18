
list_a = [1, 2, 3, 4, 5]
map_a = map(lambda x: x * 2, list_a)

for x in map_a:
    print(x)

man = {
    "name": "Bob",
    "age": "65",
    "country": "Jamaica",
}

map_man = map(lambda x: x + "," + man.get(x), man)
for x in map_man:
    print(x)