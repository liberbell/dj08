fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)

fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + " banana"
print(new_fruit)

fruits = """apple
banana
grape
"""

print(fruits)
fruit = "banana"
print(fruit[2])
print(fruit[-1])

byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

msg = "ABCDEFGABCDEFG"
print(msg.count("ABC"))

print(msg.startswith("BCD"))

msg = " ABC "
print(msg)
print(msg.strip())

msg = "ABCDEFGABCDEFABC"
print(msg.strip("CBA"))
print(msg.lstrip("CBA"))
print(msg.rstrip("CBA"))

msg = "abcABC"
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC", "FFF", 1)
print(msg_r)

msg = "hello world"
print(msg.capitalize())

msg = "hello, my name is bob"
print(msg[:5])
print(msg[6:])
print(msg[1:6])

msg = "APPLE"
print(msg.islower())
print(msg.isupper())

msg = "ABCDEABC"
print(msg.find("ABC"))