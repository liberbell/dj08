# import sys

# print(sys.path)

# import sub

# sub.sample_a()
# class_a = sub.ClassA()
# class_a.print_a()
# print(sub.VAR)

# from sub import sample_a as sa, ClassA as ca

# sa()
# ins = ca()
# ins.print_a()

# from sub import *

# print(VAR)
# sample_a()

import dir1.base1 as base1
base1.print_msg()

import dir1.base2 as base2
base2.print_msg()

from dir1.base1 import print_msg
from dir1.base2 import print_msg