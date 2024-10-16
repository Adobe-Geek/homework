line = input("Please enter string: ")
assert len(line) >= 1

last = line[-1]
new_line = last + line + last
print(new_line)
