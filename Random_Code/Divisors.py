#Create a program that asks the user for a number and then 
# prints out a list of all the divisors of that number

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
