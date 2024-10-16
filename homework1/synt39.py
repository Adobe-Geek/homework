arr = [23, 45, 67, 87, 45, 9, 4, 12, 56, 23]

print(arr)

smallest = min(i for i in arr if arr.count(i) == 1)
print(smallest)
