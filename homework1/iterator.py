a = []


def iter(start, stop):
    current = start
    while current < stop + 1:
        yield current
        current += 1


for i in iter(1, 6):
    a.append(i)
print(a)
