from random import choices

array = [78, 0, 10, 20, 30, 40]

for i in range(len(array)):
    if array[i] == 10:
        if array[i + 1] == 20:
            if array[i + 2] == 30:
                print(True)
            else:
                print(False)

# if "10, 20, 30" in str(array):
#     print(True)
# else:
#     print(False)
