arr = []

for i in range(7):
    arr.append(int(input()))

max = 0
for i in arr:
    if i % 2 != 0 and i > max:
        max = i
print("largest odd number is: ", max)
