a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if a == b:
    print(0)
elif abs(10 - a) == abs(10 - b):
    print(0)
elif abs(10 - a) < abs(10 - b):
    print(a)
else:
    print(b)
