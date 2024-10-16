arr = []

for i in range(7):
    arr.append(int(input("Enter integer: ")))

# arr_cnt = []
# for j in arr:
#     arr_cnt.append((j, arr.count(j)))
# print(set(arr_cnt))

arr_cnt = {}
for j in arr:
    arr_cnt[j] = arr_cnt.get(j, 0) + 1
print(arr_cnt)
