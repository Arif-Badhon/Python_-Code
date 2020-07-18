#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Input
name = input("Insert your name: ")
age = int(input("Insert your age: "))

#Code to get the year when he or she will turn to 100 years old
year = (100 - age) + 2019
year = str(year)
#Print the command
print(name + "you will be 100 years old in " + year)