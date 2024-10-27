arr = [23, 45, 67, 87, 45, 9, 4, 12, 56, 23, 13]

k = 3

left_shift_arr = arr[k:] + arr[:k]
right_shift_arr = arr[len(arr) - k :] + arr[: len(arr) - k]

print(left_shift_arr)
print(right_shift_arr)
