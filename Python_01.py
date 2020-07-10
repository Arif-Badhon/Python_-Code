name = input("Enter Your Name ")
age = int(input("Enter your age "))
a = 100 - age
year = int (2019 + a)
print(name + ", you will be 100 years of old in " + str(year))

#import datetime
import datetime

#asking name
name = input('Type your name:')

#asking age
age = input('Type your age:')

#get the current year
now = datetime.datetime.now()

#get difference between age x 100 years
diff = 100 - int(age)

#show exactly year that user will turn 100 years old
print('Hi '+name+" you will complete 100 years in ",(now.year+diff))