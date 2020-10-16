X = int(input())
Si = input().split()
N = int(input())

Sum = 0

for i in range (1, N+1):
    A = input().split()
    if A[0] in Si:
        Si.remove(A[0])
        Sum = Sum + int(A[1])

print (Sum)
