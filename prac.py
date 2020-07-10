#n = int(input("Enter your Number"))
nums = list(map(int, input("Enter your Number").split()))
sum = 0
for num in nums:
    sum += num
print(sum)


