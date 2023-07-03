import math

msg = "Hello world, Hello"
msg2 = msg.removeprefix("He")
msg3 = msg.replace("He", "")
print(msg2)
print(msg3)

msg = "Hello world"
print(msg.removesuffix("world"))

print(math.gcd(12, 32, 44))
print(math.lcm(12, 32, 44))

def add(a: int, b:int):
    return a + b

def print_msg(msg: str):
    print(msg.upper())

print_msg("hello")
# print_msg(21)

def print_fruits(fruits: list[str]):
    for fruit in fruits:
        print(fruit)

print_fruits(["apple", "grape"])

class ClassA:
    pass

class_a = ClassA()

def func_a(class_a: ClassA):
    pass

func_a(class_a)