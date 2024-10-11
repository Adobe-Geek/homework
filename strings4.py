array = ["up", "down", "left", "right"]
word = input("Please enter word: ")


def string_insert(array, word):
    array.insert(0, word)
    print(array)


def string_remove(array, word):
    array.remove(word)
    print(array)


string_insert(array, word)
string_remove(array, word)
