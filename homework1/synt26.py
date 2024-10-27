arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

if 2 in arr and 3 in arr[arr.index(2) :]:
    print("2 and 3 are there")
else:
    print("Condition is not met")
