
file_path = "../resources/input.csv"
f = open(file_path, mode="r", encoding="utf-8")

# line = f.read()
# print(line)

lines = f.readlines()
print(lines)
for x in lines:
    print(x.rstrip("\n"))