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
print("num_tuple ={}".format(num_tuple))

num_set = {"40", "50", "60"}
print("num_set ={}".format(num_set))

print(set(num_tuple) | num_set)

num_dict = {num_tuple: num_str}
print(len(num_list))

print(num_dict.get("myKey", "does not exist"))

num_list.extend(["50", "60"])
print(num_list)

val = input("input number:")
is_under_50 = int(val) < 50
print(is_under_50)