arr = ["Red", "Green", "", "Blue", "White"]

for el in arr:
    if el == "":
        arr.remove(el)
print(arr)
