a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if a == b:
    print(0)
elif a % 5 == b % 5:
    print(min(a, b))
else:
    print(max(a, b))
