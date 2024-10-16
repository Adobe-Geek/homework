arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

value = int(input("Enter number: "))
count = 0

for i in range(len(arr) - 1):
    if value in (arr[i], arr[i + 1]):
        count += 1
if count == (len(arr) - 1):
    print("Value is everywhere")
else:
    print("Value is not everywhere")
