from datetime import datetime

time_in = input("Enter time is in HH:MM format: ")
time_out = input("Enter time out in HH:MM format: ")
price = int(input("Enter price: "))

t1 = datetime.strptime(time_in, "%H:%M")
t2 = datetime.strptime(time_out, "%H:%M")

time_to_pay = t2 - t1
if time_to_pay.total_seconds() / 60 % 60 > 10:
    print((time_to_pay.total_seconds() / 60 // 60 + 1) * price)
else:
    print((time_to_pay.total_seconds() / 60 // 60) * price)
