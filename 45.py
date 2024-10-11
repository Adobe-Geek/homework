category = int(input("Enter category of worker: "))
service_length = int(input("Enter years of worker's service: "))

if category == 1:
    base = 3000
elif category == 2:
    base = 2000
elif category == 3:
    base = 1000

if service_length < 2:
    base = base * 0.85
elif 2 <= service_length < 5:
    base = base / 0.9 * 0.85
elif 5 <= service_length < 10:
    base = base / 0.8 * 0.85
elif service_length >= 10:
    base = base / 0.7 * 0.85

print(base)
