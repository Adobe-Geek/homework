def is_year_leap(year):
    if year % 4 != 0:
        print(year, "is not leap year")
    elif year % 4 == 0 and (year % 100 == 0 and year % 400 != 0):
        print(year, "is not leap year")
    else:
        print(year, "is leap year")


test_data = [2012, 1500, 1600, 2020]

for i in test_data:
    is_year_leap(i)
