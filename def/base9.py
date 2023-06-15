
y = 0
x = 0 if y > 0 else 1
# print(x)

lambda_a = lambda x: x * x

print(lambda_a(10))

lambda_b = lambda x, y, z = 5: x * y * z
print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))

lambda_c = lambda x, y: y if x < y else x

print(lambda_c(2, 4))