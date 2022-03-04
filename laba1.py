print('Enter the number n')
n = int(input())

i, i1, i2 = 0, 1, 1
while i < n:
    i = i1 + i2
    i1 = i2
    i2 = i

print('The first number in the Fibonacci sequence greater than n =',i)