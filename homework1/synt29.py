arr1 = [10, 20, 30, 40, 10, 10, 20]
arr2 = [10, 10, 10]

for arr in (arr1, arr2):
    if all(arr[0] == el for el in arr):
        print("All items are identical")
    else:
        print("Not all items are identical")
