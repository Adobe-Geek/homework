arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

for el in arr:
    if el == 3:
        print("Element equals 3")
    elif el == 5:
        print("Element equals 5")
    else:
        print("this is: ", el)
