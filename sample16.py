
msg = "yellow"

if msg == "blue":
    print("go")
elif msg == "red":
    print("stop")
else:
    print("warning")

age = 1
if age < 20:
    print("under 20")
elif age <= 40:
    print("under 40 and over 20")
elif age >= 60:
    print("over 60")
else:
    print("some age.")

gender = "male"
age = 30

if gender == "male" or age < 20:
    print("under 20 or male")