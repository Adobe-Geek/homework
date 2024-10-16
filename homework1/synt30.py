arr = ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]

arr1 = [el for el in arr if el.startswith("ab")]
arr2 = [el for el in arr if el.startswith("b")]

print(arr1)
print(arr2)
