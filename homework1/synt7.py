arr = [1, 2, 3, 4, 1, 2, 2, 3, 5, 6, 12]
arr2 = []

for i in range(6):
    arr2.append(int(input("Please enter integer: ")))
if arr[0] == arr2[0] or arr[-1] == arr2[-1]:
    print("true")
else:
    print("false")
