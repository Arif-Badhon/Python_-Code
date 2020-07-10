# Find a string which is reading same bacwards also
word = str(input("Enter a word: "))

if word == word[::-1]:
    print("Yes")

else:
    print("No")
