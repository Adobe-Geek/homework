def rotate_left(arr):
    return arr[1:] + arr[:1]


arr1 = [1, 2, 5]
arr2 = [1, 2, 3]
arr3 = [1, 2, 4]

for arr in (arr1, arr2, arr3):
    print(rotate_left(arr))

# arr[0], arr[1], arr[2] = arr[1], arr[2], arr[0]
# print(arr)
