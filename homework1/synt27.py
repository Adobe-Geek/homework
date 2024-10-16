arr = [10, 20, 30, 40]

ind_dict = {}
for key in arr:
    ind_dict[key] = ind_dict.get(key)
print(ind_dict)
