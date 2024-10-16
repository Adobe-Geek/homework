lst = []
for i in range(3):
    lst.append(int(input("Enter number please: ")))
if any(1 <= j <= 10 for j in lst):
    print("true")
else:
    print("false")
