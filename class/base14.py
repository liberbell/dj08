
file_path = "../resources/output.csv"

f = open(file_path, "w", encoding="utf-8", newline="\n")
f.write("aaa\nbbb")

with open(file_path, mode="w", encoding="utf-8", newline="\n")as f:
    list_a = [
        ["A", "B", "C"],
        ["a", "b", "c"]
    ]
    f.writelines(list_a[0])