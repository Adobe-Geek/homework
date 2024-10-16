arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(arr)):
    arr[i][0], arr[i][2] = arr[i][2], arr[i][0]
print(arr)
