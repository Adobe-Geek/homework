x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

if abs(x - y) <= 1 or abs(x - z) <= 1:
    if abs(x - y) > 3 or abs(x - z) > 3 or abs(y - z) > 3:
        print(True)
    else:
        print(False)
