
y = 0
x = 0 if y > 0 else 1
# print(x)

lambda_a = lambda x: x * x

print(lambda_a(10))

lambda_b = lambda x, y, z = 5: x * y * z
print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))