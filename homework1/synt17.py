arr = []

for i in range(7):
    arr.append(int(input()))

count = 0
for el in arr:
    if not el % 2:
        count += 1
print("number of even integers: ", count)
