import re

line = input("Enter math expression: ")

math = re.compile(r"^[0-9+\-*/().\s]*$")

if not math.match(line):
    print("This expression is incorrect")
else:
    print(eval(line))
