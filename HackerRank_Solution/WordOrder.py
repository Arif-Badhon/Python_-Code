#You are given n words. Some words may repeat. For each word, output its number of occurrences. 
#The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.


#python3

from collections import Counter
n = int(input())
s = []
for x in range(n):
    s.append(input())
    

d = Counter(s)

ele = d.values()

s = set(s)

print(len(s))


for value in ele:
    print(value, end=' ')
