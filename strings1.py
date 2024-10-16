import string

text = input("Please enter text: ")

print(len(text))

cnt_letter = 0
cnt_upper = 0
cnt_lower = 0
cnt_digit = 0
cnt_punct = 0
cnt_space = 0

for i in text:
    if i.isalpha():
        cnt_letter += 1
    if i.isupper():
        cnt_upper += 1
    if i.islower():
        cnt_lower += 1
    if i.isdigit():
        cnt_digit += 1
    if i in string.punctuation:
        cnt_punct += 1
    if i.isspace():
        cnt_space += 1

print("letters: ", cnt_letter)
print("upper letters: ", cnt_upper)
print("lower letters: ", cnt_lower)
print("digits: ", cnt_digit)
print("punctuation: ", cnt_punct)
print("spaces: ", cnt_space)
