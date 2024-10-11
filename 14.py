line = input("Enter line please: ")

first = line[0]
last = line[-1]
line1 = last + line[1:-1] + first
print(line1)
