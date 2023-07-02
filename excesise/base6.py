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

print(add("AA", 21))