arr = [1, 2, 3, 4, 1, 2, 2, 3, 5, 6]

# new_arr = list(set(arr))
# print(new_arr)

new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)
