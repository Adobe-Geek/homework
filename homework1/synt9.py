str1 = "Red, Green, Blue, White"
str2 = "1, 3, 4, 5, 7"

arr1 = list(str1.split(", "))
arr2 = list(map(int, str2.split(", ")))

print(arr1)
print(arr2)

# def str_to_arr(strg):
#     arr = list(strg.split(", "))
#     return arr

# for strg in (str1, str2):
#     print(str_to_arr(strg))
