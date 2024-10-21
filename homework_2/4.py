class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def func(self):
        return pow(x, n)


x = int(input("Enter x: "))
n = int(input("Enter n: "))

power = Power(x, n)

print(power.func())
