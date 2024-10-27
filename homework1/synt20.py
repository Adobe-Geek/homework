arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

ind = []

for i in range(len(arr)):
    if arr[i] == 17:
        ind.append(i)
        ind.append(i + 1)

total = 0
for i in range(len(arr)):
    if i not in ind:
        total += arr[i]
print("Sum without 17 and next item is: ", total)
