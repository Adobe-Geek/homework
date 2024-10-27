arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

six = False

for i in range(len(arr) - 2):
    if arr[i] == arr[i + 1] == 6 or arr[i] == arr[i + 2] == 6:
        six = True

if six:
    print("6 next to 6 is there")
else:
    print("6 next to 6 is not there")
