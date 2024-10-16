arr = [12, 34, 23, 56, 78, 89]
arr2 = []

for i in range(5):
    arr2.append(int(input("Please enter integer: ")))

if arr[0] == arr2[0] and arr[-1] == arr2[-1]:
    print(True)
else:
    print(False)
