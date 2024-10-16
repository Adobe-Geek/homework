arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

sum_third = sum(arr[::3])
print(sum_third)
