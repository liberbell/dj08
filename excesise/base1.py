num = 10
print(type(num))
num_str = str(num)
print(type(num_str))

num_list = [num_str, "20", "30"]
print("num_list={}".format(num_list))

num_list.append("40")
print(num_list)

num_tuple = tuple(num_list)
print(type(num_tuple))

val = input("enter the number:")
num_tuple += (val,)
print(num_tuple)