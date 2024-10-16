arr = [23, 45, 67, 87, 45, 9, 4, 12, 56, 23]

print(arr)
repet = {}
for i in arr:
    repet[i] = repet.get(i, 0) + 1
for k, v in repet.items():
    if v > 1:
        print(k)
