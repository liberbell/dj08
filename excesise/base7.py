
def check_size(size: str):
    match size:
        case "L":
            print("L size")
        case "M":
            print("M size")
        case "S":
            print("S size")

check_size("L")