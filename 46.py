num = input("Enter 4-digit number: ")

sum = 0
for i in num:
    sum += int(i)
print(sum)

for i in num:
    if num.count(i) > 1:
        print(i, "->", num.count(i))

if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
    print("Sums match")
