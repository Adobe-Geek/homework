arr = [10, 20, 30, 40, 10, 10, 20]
nums = {}

for key in arr:
    nums[key] = nums.get(key, 0) + 1
print(nums)
