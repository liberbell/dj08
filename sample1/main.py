# import sys

# print(sys.path)

# import sub

# sub.sample_a()
# class_a = sub.ClassA()
# class_a.print_a()
# print(sub.VAR)

from sub import sample_a as sa, ClassA as ca

sa()
ca()