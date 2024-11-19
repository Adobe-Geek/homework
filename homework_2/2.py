class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


leng = float(input("Enter length: "))
wid = float(input("Enter width: "))

rectangle = Rectangle(leng, wid)

print("Area is:", rectangle.area())
