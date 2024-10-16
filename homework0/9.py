lst = []
for i in range(3):
    lst.append(int(input("Enter number please: ")))
count = 0
for j in lst:
    if 1 <= j <= 10:
        count += 1
if count == 1:
    print("true")
else:
    print("false")
