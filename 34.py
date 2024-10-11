from random import choices

array = choices([i for i in range(20)], k=10)

print(array.count(5))
