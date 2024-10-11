my_file = open("C:/Users/User/homework/test.txt")

for line in my_file.readlines():
    print(line.rstrip())
my_file.close()
