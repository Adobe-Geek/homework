a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if abs(a - b) >= 20 or abs(a - c) >= 20 or abs(b - c) >= 20:
    print(True)
else:
    print(False)
