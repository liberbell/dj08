for i in range(10):
    print(i)

for _ in range(100):
    print("a")

for i in range(2, 20, 3):
    print(i)

# sample = ["John", "Paul", "George", "Ringo"]
sample = ("John", "Paul", "George", "Ringo")

for member in sample:
    print(member)

human = {
    "name": "Bob",
    "age": 22,
    "gender": "Male"
}

for h in human:
    print(h, human.get(h))

