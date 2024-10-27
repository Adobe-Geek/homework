arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

arr1 = [i for i in arr if i != 0]
print(arr1)

for j in range(len(arr) - len(arr1)):
    arr1 += [-1]
print(arr1)
