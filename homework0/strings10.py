text = input("Enter you message: ")


def palindrome(text):
    forth = text.lower().replace(" ", "")
    back = forth[::-1]
    if forth == back:
        print("palindrome!")
    else:
        print("not palindrome")


palindrome(text)
