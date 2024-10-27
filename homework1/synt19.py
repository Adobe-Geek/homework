arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

arr.remove(max(arr))
arr.remove(min(arr))
average = sum(arr) / len(arr)
print("Average is: ", average)
