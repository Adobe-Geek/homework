arr = []

for i in range(7):
    arr.append(int(input()))

if arr.count(3) == 2:
    print("3 is there twice")
elif arr.count(5) == 2:
    print("5 is there twice")
else:
    print(arr)
