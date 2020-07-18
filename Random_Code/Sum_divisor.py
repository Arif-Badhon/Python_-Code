def sum_divisors(number):
    if number == 0:
      return 0
    else:
      divisors = [1]
      for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
      return sum(divisors) 

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114