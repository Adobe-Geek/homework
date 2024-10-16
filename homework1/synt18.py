arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

result = max(arr) - min(arr)

print("difference between largest and smallest is: ", result)
