class WordBack:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        words = self.string.split()
        for el in words[::-1]:
            print(el, end=" ")


line = input("Please enter phrase: ")
result = WordBack(line)
print(result.reverse())
