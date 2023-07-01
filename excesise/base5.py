ages = {
    "Bob": 21,
    "Eric": 31
}

ages_2 = {
    "Alex": 18,
    "Elton": 38
}

ages_3 = {**ages, **ages_2}
print(ages_3)

def name_age(name, age):
    print(f"name: {name}")
    print(f"age: {age}")

man = {
    "name": "Ringo",
    "age": 14
}

name_age("George", 40)
name_age(man)