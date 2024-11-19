class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1":
            return f"Your choice: {self.menu}, Price 12.00"
        elif self.menu == "menu 2":
            return f"Your choice: {self.menu}, Price 13.40"
        else:
            return "Error in menu"


paul = Lunch("menu 1")
print(paul.menu_price())
