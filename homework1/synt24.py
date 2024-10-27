arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

three = False
five = False

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1] == 5:
        five = True
    if arr[i] == arr[i + 1] == 3:
        three = True

if three and five:
    print("Condition is not met")
elif three or five:
    print("Condition is met")
else:
    print("Condition is not met")
