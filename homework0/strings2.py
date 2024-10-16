text = input("Please enter text: ")
chr = input("Please enter character: ")

new_text = text.replace(chr, chr.upper())
print(new_text)

j = new_text.rfind(chr.upper())
print(new_text[:j])
